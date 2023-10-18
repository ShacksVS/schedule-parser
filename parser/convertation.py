import json
import re


JSON_FILE_NAME = 'normalized_schedule.json'


def split_specialties(text):
    specialties = re.findall(r'«(.*?)»|"(.*?)"', text)
    flattened_specialties = [item for sublist in specialties for item in sublist if item]

    return flattened_specialties


def convert_to_dict(cleaned_data: list, specialities: list):

    temp_data = {specialty: [] for specialty in specialities}
    data = {}

    # convert simple schedule (with one speciality)
    if len(specialities) == 1:
        data[cleaned_data[1].replace('"', "'")] = cleaned_data[2:]
        return data

    # convert schedule with 2+ specialities
    for row in cleaned_data[2:]:
        subject_name = row[2]
        match = re.search(r'\((.*?)\)', subject_name)

        if match:
            value_inside_parentheses = re.sub(r'[+,.\s]', ' ', match.group(1))

            if value_inside_parentheses[0].isupper():
                continue

            value_inside_parentheses = value_inside_parentheses.strip()

            value_inside_parentheses = value_inside_parentheses.split("  ")

            for key in temp_data.keys():
                lowercase_key = key.lower()

                if len(value_inside_parentheses) > 1:
                    if lowercase_key.startswith(value_inside_parentheses[0]) or lowercase_key.startswith(
                            value_inside_parentheses[1]):
                        temp_data[key].append(row)

                if lowercase_key.startswith(value_inside_parentheses[0]):
                    temp_data[key].append(row)

    for key, value in temp_data.items():
        data[key] = value

    return data


def convert_to_json(cleaned_data: list):
    specialities = split_specialties(cleaned_data[1])
    data = convert_to_dict(cleaned_data, specialities)

    data = {cleaned_data[0]: [{key: [
        {
            "Дисципліна, викладач": item[2],
            "День": item[0],
            "Час": item[1],
            "Група": item[3],
            "Тижні": item[4],
            "Аудиторія": item[5]
        } for item in value
    ]} for key, value in data.items()
    ]}

    try:
        create_json(data)
        print(f"Successfully created json in '{JSON_FILE_NAME}'")
    except Exception as e:
        print(e)


def create_json(json_data: json):
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
