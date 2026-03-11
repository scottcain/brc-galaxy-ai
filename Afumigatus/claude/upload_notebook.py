#!/usr/bin/env python3
"""
Upload cyp51A notebook to Galaxy using BioBlend
"""

import sys
sys.path.insert(0, '/home/claude/.local/pipx/venvs/bioblend/lib/python3.11/site-packages')

from bioblend.galaxy import GalaxyInstance
import os

def upload_notebook():
    # Galaxy configuration
    galaxy_url = "https://usegalaxy.org"
    api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
    history_id = "bbd44e69cb8906b56e8fabc27d17fcce"  # A fumigatus antifungal resistance analysis

    # Notebook file
    notebook_path = "/workspace/AfumigatusII/cyp51A_SNP_analysis_v8_1.ipynb"

    print(f"Connecting to Galaxy at {galaxy_url}...")

    try:
        # Connect to Galaxy
        gi = GalaxyInstance(galaxy_url, key=api_key)

        # Verify connection
        user = gi.users.get_current_user()
        print(f"✓ Connected as user: {user['username']}")

        # Get history info
        history = gi.histories.show_history(history_id)
        print(f"✓ Target history: {history['name']}")

        # Upload notebook
        print(f"Uploading notebook: {notebook_path}")

        upload_result = gi.tools.upload_file(
            path=notebook_path,
            history_id=history_id,
            file_name="cyp51A_SNP_analysis_v8_1_snpeff_annotated.ipynb",
            file_type="auto"
        )

        print(f"✓ Upload successful!")
        print(f"Dataset ID: {upload_result['outputs'][0]['id']}")
        print(f"Dataset Name: {upload_result['outputs'][0]['name']}")

        # Get updated history info
        history_contents = gi.histories.show_history(history_id, contents=True)
        dataset_count = len([item for item in history_contents if item['history_content_type'] == 'dataset'])
        print(f"✓ History now contains {dataset_count} datasets")

        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = upload_notebook()
    sys.exit(0 if success else 1)