from bioblend.galaxy import GalaxyInstance
import json
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
history_id = "bbd44e69cb8906b5623ea083aa036a1d"

datasets = gi.histories.show_history(history_id, contents=True)
collections = [d for d in datasets if d["history_content_type"] == "dataset_collection"]

print(f"Number of collections: {len(collections)}")
for c in collections:
    print(f"Collection: {c['name']}")
