from bioblend.galaxy import GalaxyInstance
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)

history_name = "A. fumigatus variants"
histories = gi.histories.get_histories(name=history_name)

if histories:
    history = histories[0]
    history_id = history['id']
    datasets = gi.histories.show_history(history_id, contents=True)
    print(f"History: {history['name']} (ID: {history_id})")
    print(f"Number of datasets: {len(datasets)}")
else:
    print(f"History '{history_name}' not found.")
