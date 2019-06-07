json_file = {'status': 1, 'count': 1, 'data': {'networks': [{'7': 'Affiliate Window'}, {'83': 'Magic Links'}, {'46': 'Skimlinks'}]}, 'extra': {'networks_short_name': [{'7': 'AWIN'}, {'83': 'MLK'}, {'46': 'SL'}]}}
import pandas as pd

file_r = pd.read_json(json_file)['data']
print(file_r)

