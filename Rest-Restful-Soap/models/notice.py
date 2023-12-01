from bs4 import BeautifulSoup
import requests
class Notice:
    def __init__(self,name,url):
        self.name = name
        self.url = url
        self.year = ''
        self.number = ''
        self.situation = ''
        self.modality = ''
        self.pdf_link = ''

    def __init__(self, id, title, url, year, number, situation, modality, pdf_link):
        self.id = id
        self.title = title
        self.url = url
        self.year = year
        self.number = number
        self.situation = situation
        self.modality = modality
        self.pdf_link = pdf_link



    def to_json(self,) -> dict:
        return{
            'name' : self.name,
            'url' : self.url,
            'year': self.year,
            'number' : self.number,
            'situation' : self.situation,
            'modality' : self.modality,
            'pdf_link' : self.pdf_link
        }
    
    def update_notice(self,soup:BeautifulSoup):
        self.modality = soup.find(id='form-widgets-modalidade_edital').find(class_='selected-option').text
        self.number = soup.find(id='form-widgets-numero_edital').text
        self.year = soup.find(id='form-widgets-ano_edital').text.replace('.','')
        self.situation = soup.find(id='form-widgets-situacao_edital').find(class_='selected-option').text

        noticePdfPage = ''

        tbody_tag = soup.find('tbody')

        tr_tags = tbody_tag.find_all('tr')
        for tr in tr_tags:
            td_tags = tr.find_all('td')
            if (td_tags[1] and 'Arquivo' in td_tags[1].text):
                noticePdfPage = td_tags[0].find('a').get('href')
                break

        response = requests.get(noticePdfPage)

        if not response:
            return None

        self.pdf_link = BeautifulSoup(response.content, 'html.parser').find(
            id='content-core').find('a').get('href')
