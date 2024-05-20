import os
import json
import csv
from datetime import datetime

def is_date(filename):
    try:
        datetime.strptime(filename.split('.')[0], '%Y-%m-%d')
        return True
    except ValueError:
        return False

def process_json_file(filepath):
    result = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line)
                for key, value in data.items():
                    first_class = value.get("FirstClassification", {})
                    second_class = value.get("SecondClassification", {})
                    third_class = value.get("ThirdClassification", {})
                    result.append({
                        "Title": key,
                        "FirstClassificationId": first_class.get("Id", ""),
                        "FirstClassificationLabel": first_class.get("Label", ""),
                        "FirstClassificationName": first_class.get("Name", ""),
                        "FirstClassificationScore": first_class.get("Score", ""),
                        "SecondClassificationId": second_class.get("Id", ""),
                        "SecondClassificationLabel": second_class.get("Label", ""),
                        "SecondClassificationName": second_class.get("Name", ""),
                        "SecondClassificationScore": second_class.get("Score", ""),
                        "ThirdClassificationId": third_class.get("Id", "") if third_class else "",
                        "ThirdClassificationLabel": third_class.get("Label", "") if third_class else "",
                        "ThirdClassificationName": third_class.get("Name", "") if third_class else "",
                        "ThirdClassificationScore": third_class.get("Score", "") if third_class else "",
                        "RequestId": value.get("RequestId", "")
                    })
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filepath}: {e}")
                continue
    return result

def main(output_directory, output_csv):
    all_data = []
    for filename in os.listdir(output_directory):
        if filename.endswith(".json") and is_date(filename):
            filepath = os.path.join(output_directory, filename)
            all_data.extend(process_json_file(filepath))
    
    if all_data:
        keys = all_data[0].keys()
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(all_data)

if __name__ == "__main__":
    output_directory = './output'  
    output_csv = 'output_summary.csv'
    main(output_directory, output_csv)
