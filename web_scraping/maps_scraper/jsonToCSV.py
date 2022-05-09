
import json
import csv

def json_to_csv(file_path, csv_name) -> None:
    with open(file_path) as json_file:
        data = json.load(json_file)
        headers = data[0].keys()

        with open(csv_name, 'w') as csv_file_local:
            writer = csv.writer(csv_file_local)
            writer.writerow(headers)

            for record in data:
                rec = (value for value in record.values())
                writer.writerow(rec)


if __name__ == '__main__':
    import sys
    import pathlib
    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]
    except IndexError:
        sys.exit("Two arguments requires, one json file path and one save file name")
    
    with pathlib.Path(file_path) as json_file_global:
        if json_file_global.is_file():
            json_to_csv(file_path, csv_name)

        print(f'Did not find {file_path}')