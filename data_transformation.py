"""
Преобразование CSV файлов в JSON формат
"""

import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    jsonArray = []
    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            pk = row["Id"]
            model_name = "ads.ads"
            # model_name = "ads.category"
            row.pop("Id")
            if row["is_published"] == "TRUE":
                row["is_published"] = True
            elif row["is_published"] == "FALSE":
                row["is_published"] = False
            row["price"] = int(row["price"])
            new_row = {
                "model": model_name,
                "pk": pk,
                "fields": row
            }
            jsonArray.append(new_row)

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)


csv_file_path = r'datasets/ads.csv'
json_file_path = r'fixtures/ads.json'

# csv_file_path = r'datasets/categories.csv'
# json_file_path = r'fixtures/categories.json'

csv_to_json(csv_file_path, json_file_path)
