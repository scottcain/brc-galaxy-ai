from bioblend.galaxy import GalaxyInstance
api_key = "1ec16146319180142ee10b98cfb09cca"
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
history_id = "bbd44e69cb8906b5623ea083aa036a1d"
gi.tools.upload_file("variants_cyp51A_v9.ipynb", history_id, file_type="ipynb")
print("Uploaded variants_cyp51A_v9.ipynb to history:", history_id)
