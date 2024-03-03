import json
import openpyxl

def json_to_excel(json_file, excel_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)

        if not data:
            print("The JSON file is empty.")
            return

        if not isinstance(data, list):
            print("The JSON structure is not a list. Further processing is needed.")
            return

        wb = openpyxl.Workbook()
        ws = wb.active

        # Adding header
        header = data[0].keys()
        ws.append(header)

        # Adding data
        for row in data:
            ws.append(row.values())

        wb.save(excel_file)

    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding the JSON file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

json_file = #path to json file
excel_file = #path to excel file

json_to_excel(json_file, excel_file)
