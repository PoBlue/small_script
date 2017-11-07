from utils import helper

dir_path = "/Users/moweiquan/Desktop/auto-review/regex_review/data/"
file_counter = 0

for file_path in helper.get_path_json_from_dir(dir_path):
    json_data = helper.get_json_from_file(file_path)

    for review in json_data['reviews']:
        review['isMatch'] = True
    
    print("current: %d" % file_counter)
    file_counter += 1
    helper.write_json_to_file(file_path, json_data)

print("All counter %d" % file_counter)