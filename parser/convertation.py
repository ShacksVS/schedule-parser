import json


JSON_FILE_NAME = 'normalized_schedule.json'


def convert_to_json(cleaned_data: list):
    data = {
        cleaned_data[0]: {
            cleaned_data[1].replace('"', "'"): [
                {
                    "Дисципліна, викладач": item[2],
                    "День": item[0],
                    "Час": item[1],
                    "Група": item[3],
                    "Тижні": item[4],
                    "Аудиторія": item[5]
                }
                for item in cleaned_data[3:]
            ]
        }
    }

    try:
        create_json(data)
        print(f"Successfully created json in '{JSON_FILE_NAME}'")
    except Exception as e:
        print(e)


def create_json(json_data: json):
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
