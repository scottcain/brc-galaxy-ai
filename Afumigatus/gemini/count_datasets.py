from bioblend.galaxy import GalaxyInstance
import os
api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
history_id = "bbd44e69cb8906b50c94e6b73207d261"
datasets = gi.histories.show_history(history_id, contents=True)
print(f"Number of datasets in history '{history_id}': {len(datasets)}")
