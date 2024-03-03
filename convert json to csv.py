import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as jf:  # Added encoding='utf-8'
            data = json.load(jf)
        
        if not data:
            print("The JSON file is empty.")
            return

        # If the JSON is not a list, you may need to adjust the code accordingly
        if not isinstance(data, list):
            print("The JSON structure is not a list. Further processing is needed.")
            return

        with open(csv_file, 'w', newline='', encoding='utf-8') as cf:  # Added encoding='utf-8'
            writer = csv.writer(cf)
            header = data[0].keys()
            writer.writerow(header)
            for row in data:
                writer.writerow(row.values())
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding the JSON file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

json_file = # Input JSON file
csv_file = # Output CSV file

json_to_csv(json_file, csv_file)
