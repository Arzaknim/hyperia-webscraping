import json


def save_to_json(name: str, list_of_job_dicts: list) -> None:
    try:
        print('Saving the file.....')
        with open(f'{name}.json', 'w') as jsonFile:
            jsonFile.write('[\n')
            for entry in list_of_job_dicts:
                if entry == list_of_job_dicts[-1]:
                    jsonFile.write(json.dumps(entry, indent=4) + '\n')
                else:
                    jsonFile.write(json.dumps(entry, indent=4) + ',\n')
            jsonFile.write(']\n')
        print('Done')
    except Exception as e:
        print(f'Something wrong happened while trying to write to a json file, {e}')
