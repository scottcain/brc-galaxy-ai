from bioblend.galaxy import GalaxyInstance
api_key = "d8768fb7ed9cd6c0f29e27df424bc3d4"
gi = GalaxyInstance(url="https://usegalaxy.org", key=api_key)
history_id = "bbd44e69cb8906b5623ea083aa036a1d"
gi.tools.upload_file("variants_cyp51A_v20.ipynb", history_id, file_type="ipynb")
print("Uploaded variants_cyp51A_v20.ipynb to history:", history_id)
