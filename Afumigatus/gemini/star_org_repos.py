import os
import sys
import time
import argparse
import httpx

def get_headers(token):
    return {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }

def handle_rate_limit(response):
    """Check for rate limits and sleep if necessary. Returns True if rate limited."""
    if (response.status_code in (403, 429) and 'rate limit' in response.text.lower()) or \
       (response.headers.get('x-ratelimit-remaining') == '0'):
        reset_time = int(response.headers.get("x-ratelimit-reset", time.time() + 60))
        sleep_time = max(reset_time - time.time(), 0) + 1
        print(f"\nRate limit hit. Sleeping for {int(sleep_time)} seconds...")
        time.sleep(sleep_time)
        return True
    return False

def get_org_repos(org_name, headers):
    """Fetch all repositories for the given organization."""
    url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"
    repos = []
    
    while url:
        response = httpx.get(url, headers=headers)
        if handle_rate_limit(response):
            continue
            
        response.raise_for_status()
        repos.extend(response.json())
        
        # Pagination check
        link_header = response.headers.get("link")
        url = None
        if link_header:
            for link in link_header.split(","):
                if 'rel="next"' in link:
                    url = link[link.find("<")+1:link.find(">")]
                    break
    return repos

def is_starred(owner, repo, headers):
    """Check if the authenticated user has already starred the repository."""
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    while True:
        response = httpx.get(url, headers=headers)
        if handle_rate_limit(response):
            continue
            
        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            return False
        else:
            response.raise_for_status()

def star_repo(owner, repo, headers):
    """Star the repository for the authenticated user."""
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    while True:
        response = httpx.put(url, headers=headers)
        if handle_rate_limit(response):
            continue
            
        response.raise_for_status()
        return

def main():
    parser = argparse.ArgumentParser(description="Star all repositories in a GitHub organization.")
    parser.add_argument("org_name", help="The name of the GitHub organization")
    args = parser.parse_args()
    
    # Check for GITHUB_APP_KEY or GITHUB_TOKEN
    token = os.environ.get("GITHUB_APP_KEY") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: Please set the GITHUB_APP_KEY or GITHUB_TOKEN environment variable.")
        print("Example: export GITHUB_APP_KEY='your_token_here'")
        sys.exit(1)
        
    headers = get_headers(token)
    org_name = args.org_name
    
    print(f"Fetching repositories for organization: {org_name}...")
    try:
        repos = get_org_repos(org_name, headers)
    except httpx.HTTPStatusError as e:
        print(f"Error fetching repositories: {e}")
        if e.response.status_code == 404:
            print(f"Organization '{org_name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching repositories: {e}")
        sys.exit(1)
        
    print(f"Found {len(repos)} repositories. Checking and starring...")
    
    starred_count = 0
    already_starred_count = 0
    
    for i, repo in enumerate(repos, 1):
        repo_name = repo["name"]
        owner = repo["owner"]["login"]
        print(f"[{i}/{len(repos)}] {repo_name}...", end=" ", flush=True)
        
        try:
            if is_starred(owner, repo_name, headers):
                print("Already starred.")
                already_starred_count += 1
            else:
                star_repo(owner, repo_name, headers)
                print("Starred!")
                starred_count += 1
        except Exception as e:
            print(f"Error: {e}")
            
    print(f"\nFinished!")
    print(f"Newly starred: {starred_count}")
    print(f"Already starred: {already_starred_count}")

if __name__ == "__main__":
    main()
