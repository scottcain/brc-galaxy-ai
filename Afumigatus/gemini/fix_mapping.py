with open("notebook_source.py", "r") as f:
    code = f.read()

import re

new_mapping_code = """
mapping = {}
for item in contents:
    if item.get('history_content_type') == 'dataset_collection':
        col_id = item.get('collection_id') or item.get('id')
        try:
            col_data = await gxy.api(f"/api/dataset_collections/{col_id}")
            elements = col_data.get('elements', [])
            for el in elements:
                obj = el.get('object', {})
                ds_id = obj.get('id')
                hid = obj.get('hid')
                uuid_val = obj.get('uuid')
                identifier = el.get('element_identifier')
                if identifier:
                    if ds_id: mapping[ds_id] = identifier
                    if uuid_val: mapping[uuid_val] = identifier
                    if hid: mapping[f"Galaxy{hid}-"] = identifier
                    # gxy sometimes uses dataset_UUID or dataset_ID
                    if ds_id: mapping[f"dataset_{ds_id}"] = identifier
                    if uuid_val: mapping[f"dataset_{uuid_val}"] = identifier
        except Exception as e:
            pass
"""

# Replace the mapping logic block
code = re.sub(
    r'mapping = \{\}.*?except Exception as e:\n            pass',
    new_mapping_code.strip(),
    code,
    flags=re.DOTALL
)

with open("notebook_source.py", "w") as f:
    f.write(code)
