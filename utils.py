import csv
import json

from configuration import config


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    with open(csv_file_path, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row_keys = [x.lower() for x in list(row.keys())]
            edited_row = dict(zip(row_keys, list(row.values())))
            json_array.append(edited_row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_data = json.dumps(json_array, ensure_ascii=False, indent=4)
        json_file.write(json_data)


csv_to_json(config.AD_ROOT_CSV, config.AD_ROOT_JSON)
csv_to_json(config.CATEGORY_ROOT_CSV, config.CATEGORY_ROOT_JSON)
csv_to_json(config.LOCATION_ROOT_CSV, config.LOCATION_ROOT_JSON)
csv_to_json(config.USER_ROOT_CSV, config.USER_ROOT_JSON)
