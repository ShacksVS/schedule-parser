import json


def convert_to_json(cleaned_data: list) -> json:
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

    return data


def create_json(json_data: json):
    with open('normalized_schedule.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
