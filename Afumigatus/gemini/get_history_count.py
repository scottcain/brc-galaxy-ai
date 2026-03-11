from bioblend.galaxy import GalaxyInstance
import os
api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
histories = gi.histories.get_histories(name="Working copy of BRC Analytics - A. fumigatus Azole Resistance")
if not histories:
    histories = gi.histories.get_histories()
    for h in histories:
        if "fumigatus" in h['name']:
            print("Found history:", h['name'], h['id'])
            history_id = h['id']
            break
else:
    history_id = histories[0]['id']

datasets = gi.histories.show_history(history_id, contents=True)
print(f"Number of datasets in history: {len(datasets)}")
