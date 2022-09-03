from bs4 import BeautifulSoup
import requests


def get_list_of_links(url: str) -> list:
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        positions = soup.find_all('section', {'id': 'positions'})
        links_to_jobs = positions[0].find_all('a', {'class': 'arrow-link'})
        return links_to_jobs
    except Exception as e:
        print(f'Something wrong happened while getting the links to one of the empty positions, {e}')


def get_list_of_dictionaries(url: str) -> list:
    try:
        print('Getting the dictionary objects.....')
        json_list = []
        for link in get_list_of_links(url):
            job_url = url.split('/kariera')[0] + link.attrs['href']
            job_req = requests.get(job_url)
            job_soup = BeautifulSoup(job_req.text, 'html.parser')
            title = job_soup.find('div', {'class': 'hero-text col-lg-12'}).h1.text
            columns = job_soup.find('section', {'class': 'position-hero'}).find('div', {'class': 'row'}).find_all('div', {
                'class': 'col-md-4 icon'})
            place = columns[0].text.split(':')[1]
            salary = columns[1].text.split('PlatovÃ© ohodnotenie')[1]
            contract = columns[2].text.split('Typ pracovÃ©ho pomeru')[1]

            contact = job_soup.find('div', {'class': 'container position-contact'}).strong.text
            job_object = {'title': title, 'place': place, 'salary': salary, 'contract_type': contract, 'contact_email': contact}
            json_list.append(job_object)
        print('Done')
        return json_list
    except Exception as e:
        print(f'Something wrong happened while working on the list of dictionaries, {e}')
