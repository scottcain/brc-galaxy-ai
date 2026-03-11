import asyncio
from bioblend.galaxy import GalaxyInstance
import sys
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)
history_id = "bbd44e69cb8906b50c94e6b73207d261"

collections = gi.histories.show_history(history_id, contents=True, types=['dataset_collection'])
if collections:
    col = collections[0]
    col_id = col['id']
    try:
        col_data1 = gi.make_get_request(f"{gi.url}/api/dataset_collections/{col_id}").json()
        print(f"API 1 Success! keys: {list(col_data1.keys())}")
    except Exception as e:
        print(f"API 1 Failed: {e}")
        
    try:
        col_data2 = gi.make_get_request(f"{gi.url}/api/histories/{history_id}/contents/dataset_collections/{col_id}").json()
        print(f"API 2 Success! keys: {list(col_data2.keys())}")
    except Exception as e:
        print(f"API 2 Failed: {e}")
