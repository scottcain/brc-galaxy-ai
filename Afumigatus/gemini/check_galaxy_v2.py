from bioblend.galaxy import GalaxyInstance
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)

# The specific history requested in STEP1-generic.md
history_slug_or_name = "a-fumigatus-variants"

histories = gi.histories.get_histories()
history = next((h for h in histories if history_slug_or_name in h.get('slug', '') or history_slug_or_name in h.get('name', '').lower().replace(' ', '-')), None)

# fallback to checking exact name if above fails
if not history:
    history = next((h for h in histories if h['name'] == 'a-fumigatus-variants' or h['name'] == 'A fumigatus variants'), None)

if history:
    history_id = history['id']
    datasets = gi.histories.show_history(history_id, contents=True)
    print(f"History: {history['name']} (ID: {history_id})")
    print(f"Number of datasets: {len(datasets)}")
else:
    print(f"History '{history_slug_or_name}' not found.")
    print("Available histories:")
    for h in histories[:5]: # print first 5
        print(f"- {h['name']} (slug: {h.get('slug')})")

