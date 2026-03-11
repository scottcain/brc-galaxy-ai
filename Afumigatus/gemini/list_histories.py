from bioblend.galaxy import GalaxyInstance
import os
api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
histories = gi.histories.get_histories()
for h in histories:
    print(f"ID: {h['id']}, Name: {h['name']}")
