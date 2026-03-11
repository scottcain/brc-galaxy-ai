from bioblend.galaxy import GalaxyInstance
import sys
import os

# Connect to Galaxy
api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)

# Find the history
histories = gi.histories.get_histories(name="A fumigatus antifungal resistance analysis")
if not histories:
    histories = gi.histories.get_histories()
    history = next((h for h in histories if "Azole resistance analysis" in h['name']), None)
else:
    history = histories[0]

if not history:
    print("History not found.")
    sys.exit(1)

history_id = history['id']
print(f"Uploading to history: {history['name']} (ID: {history_id})")

# Upload the notebook
try:
    res = gi.tools.upload_file(
        "resistant_specific_snps.ipynb", 
        history_id, 
        file_name="Step4: Resistant Specific SNPs Notebook", 
        file_type="ipynb"
    )
    print("Uploaded successfully!")
except Exception as e:
    print(f"Failed to upload: {e}")
