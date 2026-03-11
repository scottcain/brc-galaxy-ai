import asyncio
from bioblend.galaxy import GalaxyInstance
import sys
import os

api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
gi = GalaxyInstance(url='https://usegalaxy.org', key=api_key)
history_id = "bbd44e69cb8906b50c94e6b73207d261"

datasets = gi.histories.show_history(history_id, contents=True)
snpeff_ds = None
for ds in datasets:
    if ds.get('state') == 'ok' and 'SnpEff eff:' in ds['name']:
        snpeff_ds = ds
        break

if snpeff_ds:
    print(f"Downloading {snpeff_ds['name']} (ID: {snpeff_ds['id']})...")
    try:
        gi.datasets.download_dataset(snpeff_ds['id'], file_path="/app/sample_snpeff.vcf", use_default_filename=False)
        print("Downloaded.")
    except Exception as e:
        print(f"Download failed: {e}")
else:
    print("No SnpEff VCF found.")
