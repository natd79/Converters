import json
import csv

def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as cf:
            reader = csv.DictReader(cf)
            data = [row for row in reader]
        
        if not data:
            print("The CSV file is empty.")
            return

        with open(json_file, 'w', encoding='utf-8') as jf:
            json.dump(data, jf, ensure_ascii=False, indent=4)
            
        print(f"Conversion complete. JSON data has been saved to '{json_file}'.")
            
    except csv.Error as e:
        print(f"An error occurred while reading the CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

csv_file =  #Path to CSV file
json_file = #Path to JSON file

csv_to_json(csv_file, json_file)