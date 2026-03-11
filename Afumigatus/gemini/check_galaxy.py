from bioblend.galaxy import GalaxyInstance
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)

# List histories and find the one that matches "A.fumigatus Azole resistance analysis" or similar
histories = gi.histories.get_histories(name="A fumigatus antifungal resistance analysis")
if not histories:
    # Try case-insensitive or partial match if exact name fails
    histories = gi.histories.get_histories()
    history = next((h for h in histories if "Azole resistance analysis" in h['name']), None)
else:
    history = histories[0]

if history:
    history_id = history['id']
    datasets = gi.histories.show_history(history_id, contents=True)
    print(f"History: {history['name']} (ID: {history_id})")
    print(f"Number of datasets: {len(datasets)}")
else:
    print("History not found.")
