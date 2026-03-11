#!/usr/bin/env python3
"""
Use Galaxy MCP server to inspect collections #450 and #351
and get individual dataset IDs for VCF files
"""

import sys
sys.path.insert(0, '/home/claude/.local/pipx/venvs/bioblend/lib/python3.11/site-packages')

from bioblend.galaxy import GalaxyInstance
import json

def get_collection_datasets():
    # Galaxy configuration
    galaxy_url = "https://usegalaxy.org"
    api_key = os.environ.get("GALAXY_API_KEY")
if not api_key:
    raise ValueError("GALAXY_API_KEY environment variable not set. Set it with: export GALAXY_API_KEY='your_key'")
    history_id = "bbd44e69cb8906b56e8fabc27d17fcce"  # A fumigatus antifungal resistance analysis

    print(f"Connecting to Galaxy at {galaxy_url}...")

    try:
        # Connect to Galaxy
        gi = GalaxyInstance(galaxy_url, key=api_key)

        # Verify connection
        user = gi.users.get_current_user()
        print(f"✓ Connected as user: {user['username']}")

        # Get history contents
        print(f"Getting history contents...")
        history_contents = gi.histories.show_history(history_id, contents=True)

        print(f"✓ History contains {len(history_contents)} items")

        # Look for collections #450 and #351 (or around those numbers)
        target_collections = [450, 451, 449, 452, 350, 351, 352, 353]  # Search around target numbers

        print(f"\nSearching for collections around #450 and #351...")

        found_collections = []
        individual_datasets = []

        for item in history_contents:
            hid = item.get('hid', 0)
            name = item.get('name', '')
            history_content_type = item.get('history_content_type', '')

            # Look for collections around target HIDs
            if hid in target_collections:
                print(f"\n📁 HID {hid}: {name} ({history_content_type})")

                if history_content_type == 'dataset_collection':
                    found_collections.append(item)
                    print(f"  🎯 COLLECTION FOUND!")

                    # Get collection details
                    try:
                        collection_id = item['id']
                        collection_details = gi.dataset_collections.show_dataset_collection(collection_id)

                        print(f"  Collection ID: {collection_id}")
                        print(f"  Collection type: {collection_details.get('collection_type', 'N/A')}")
                        print(f"  Elements: {len(collection_details.get('elements', []))}")

                        # List collection elements
                        elements = collection_details.get('elements', [])
                        for j, element in enumerate(elements[:5], 1):  # Show first 5 elements
                            element_name = element.get('element_identifier', f'element_{j}')
                            element_type = element.get('element_type', 'N/A')

                            print(f"    {j}: {element_name} ({element_type})")

                            # If it's a dataset, get its HID
                            if element_type == 'hda':  # History Dataset Association
                                dataset_info = element.get('object', {})
                                dataset_hid = dataset_info.get('hid', 'N/A')
                                dataset_id = dataset_info.get('id', 'N/A')
                                dataset_name = dataset_info.get('name', 'N/A')

                                print(f"      → HID {dataset_hid}: {dataset_name}")
                                print(f"      → Dataset ID: {dataset_id}")

                                # Check if it's a VCF file
                                if any(vcf_indicator in dataset_name.lower() for vcf_indicator in ['vcf', 'variant']):
                                    individual_datasets.append({
                                        'collection_hid': hid,
                                        'dataset_hid': dataset_hid,
                                        'dataset_id': dataset_id,
                                        'dataset_name': dataset_name,
                                        'collection_name': name
                                    })
                                    print(f"      ✓ VCF dataset identified!")

                        if len(elements) > 5:
                            print(f"    ... and {len(elements) - 5} more elements")

                    except Exception as e:
                        print(f"  ✗ Error getting collection details: {e}")

                elif history_content_type == 'dataset':
                    # Individual dataset around target numbers
                    if any(vcf_indicator in name.lower() for vcf_indicator in ['vcf', 'variant']):
                        individual_datasets.append({
                            'collection_hid': None,
                            'dataset_hid': hid,
                            'dataset_id': item['id'],
                            'dataset_name': name,
                            'collection_name': None
                        })
                        print(f"  🎯 Individual VCF dataset found!")

        # Also look for VCF files in the general vicinity
        print(f"\nScanning for VCF files in HID range 300-500...")
        vcf_datasets_found = 0

        for item in history_contents:
            hid = item.get('hid', 0)
            name = item.get('name', '')
            history_content_type = item.get('history_content_type', '')

            if (300 <= hid <= 500 and
                history_content_type == 'dataset' and
                any(vcf_indicator in name.lower() for vcf_indicator in ['vcf', 'variant', 'call'])):

                individual_datasets.append({
                    'collection_hid': None,
                    'dataset_hid': hid,
                    'dataset_id': item['id'],
                    'dataset_name': name,
                    'collection_name': None
                })
                vcf_datasets_found += 1

                if vcf_datasets_found <= 10:  # Show first 10
                    print(f"  HID {hid}: {name}")

        if vcf_datasets_found > 10:
            print(f"  ... and {vcf_datasets_found - 10} more VCF datasets")

        # Summary
        print(f"\n" + "="*60)
        print(f"COLLECTION ANALYSIS SUMMARY")
        print(f"="*60)
        print(f"Collections found: {len(found_collections)}")
        print(f"VCF datasets identified: {len(individual_datasets)}")

        if len(individual_datasets) > 0:
            print(f"\nVCF DATASETS FOR NOTEBOOK:")
            for i, dataset in enumerate(individual_datasets[:10], 1):
                print(f"  {i}. HID {dataset['dataset_hid']}: {dataset['dataset_name']}")
                print(f"     ID: {dataset['dataset_id']}")
                if dataset['collection_name']:
                    print(f"     From collection: {dataset['collection_name']}")

        # Save results for notebook use
        with open('vcf_datasets.json', 'w') as f:
            json.dump(individual_datasets, f, indent=2)

        print(f"\n✓ Results saved to 'vcf_datasets.json'")
        print(f"✓ Ready to create v6 notebook with individual dataset IDs")

        return individual_datasets

    except Exception as e:
        print(f"✗ Error: {e}")
        return []

if __name__ == "__main__":
    datasets = get_collection_datasets()
    print(f"\nFound {len(datasets)} VCF datasets for notebook integration")