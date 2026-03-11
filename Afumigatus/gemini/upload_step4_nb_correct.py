from bioblend.galaxy import GalaxyInstance
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)
correct_history_id = "bbd44e69cb8906b50c94e6b73207d261"

print(f"Uploading to Step 1 history: {correct_history_id}")
res = gi.tools.upload_file(
    "resistant_specific_snps.ipynb", 
    correct_history_id, 
    file_name="Step4: Resistant Specific SNPs Notebook", 
    file_type="ipynb"
)
print("Uploaded successfully!")
