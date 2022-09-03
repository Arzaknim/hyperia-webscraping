import webscraper
import file_service

URL = 'https://www.hyperia.sk/kariera'
FILENAME = 'hyperia'

if __name__ == '__main__':
    list_of_job_dicts = webscraper.get_list_of_dictionaries(URL)
    file_service.save_to_json(FILENAME, list_of_job_dicts)

