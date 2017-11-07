import json
import glob

# get json from file
def get_json_from_file(file_path):
    with open(file_path) as json_data:
        d = json.load(json_data)
        return d

def get_path_json_from_dir(dir_path):
    return glob.glob(dir_path + '*.json')

# wirte json to file
def write_json_to_file(file_path, json_data):
    with open(file_path, 'w') as outfile:  
        json.dump(json_data, outfile)

