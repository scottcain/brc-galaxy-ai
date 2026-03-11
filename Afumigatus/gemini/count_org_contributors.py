import httpx
import os
import sys
import time

# You must set your GITHUB_TOKEN environment variable before running this
TOKEN = os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("Error: Please set the GITHUB_TOKEN environment variable.")
    print("Run: export GITHUB_TOKEN='your_personal_access_token'")
    sys.exit(1)

ORG_NAME = "galaxyproject"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}"
}

def get_paginated_data(url):
    """Fetch all pages from a GitHub API paginated endpoint."""
    results = []
    while url:
        response = httpx.get(url, headers=HEADERS)
        if response.status_code == 403 and 'rate limit' in response.text.lower():
            reset_time = int(response.headers.get("x-ratelimit-reset", time.time() + 60))
            sleep_time = max(reset_time - time.time(), 0) + 1
            print(f"\nRate limit hit. Sleeping for {int(sleep_time)} seconds...")
            time.sleep(sleep_time)
            continue
            
        response.raise_for_status()
        results.extend(response.json())
        
        # Check for the 'next' page link in the headers
        link_header = response.headers.get("link")
        url = None
        if link_header:
            links = link_header.split(",")
            for link in links:
                if 'rel="next"' in link:
                    url = link[link.find("<")+1:link.find(">")]
                    break
    return results

def main():
    print(f"Fetching repositories for organization: {ORG_NAME}...")
    repos_url = f"https://api.github.com/orgs/{ORG_NAME}/repos?per_page=100"
    repos = get_paginated_data(repos_url)
    
    print(f"Found {len(repos)} repositories. Fetching contributors for each...")
    
    unique_contributors = set()
    
    for i, repo in enumerate(repos, 1):
        repo_name = repo["name"]
        print(f"[{i}/{len(repos)}] Processing {repo_name}...", end="")
        
        # Some repos might be empty, so we catch 404s on the contributors endpoint
        contrib_url = f"https://api.github.com/repos/{ORG_NAME}/{repo_name}/contributors?per_page=100"
        try:
            contributors = get_paginated_data(contrib_url)
            for user in contributors:
                if "login" in user:
                    unique_contributors.add(user["login"])
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                # 404 usually means the repository is completely empty
                continue
            elif e.response.status_code == 204:
                continue
            else:
                print(f"\nError fetching {repo_name}: {e}")
                
    print(f"\n\nFinished!")
    print(f"Total unique contributors to {ORG_NAME}: {len(unique_contributors)}")

if __name__ == "__main__":
    main()