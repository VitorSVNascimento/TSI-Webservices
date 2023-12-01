import requests
from models.notice import Notice
from constants import *
import bs4
import os
import argparse
from concurrent.futures import ThreadPoolExecutor
from DAO import noticeDAO as dao

noticies = []

def find_all_noticies():
    if(not os.path.exists(dao.DATABASE_NAME)):
         fill_database()
    get_filter_noticies()
    
def get_filter_noticies():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ano", "--ano", help="ano")
    parser.add_argument("-modalidade", "--modalidade", help="modalidade")
    parser.add_argument("-numero", "--numero", help="numero")
    parser.add_argument("-situacao", "--situacao", help="situacao")
    parser.add_argument("terms", nargs="*", help="termos de busca")
    args = parser.parse_args()

    year = args.ano
    modality = args.modalidade
    number = args.numero
    situation = args.situacao
    terms = args.terms
    
    notice_list = dao.get_by_filters(year,modality,number,situation,terms)
    results_to_string(notice_list)



def results_to_string(results):
    print(f'{len(results)} resultados')
    print('-----------------------')
    for result in results:
        print(f'Edital: {result.title}')
        print(f'Link: {result.pdf_link}')
    pass

def fill_database():
    links = get_links_list()

    [noticies.append(Notice(link.text.strip(),link.get('href'))) for link in links]

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(get_notice_informations, noticies)

    dao.create_table()
    [dao.insert(notice) for notice in noticies]


def get_links_list():
    JUMP = 30
    page = 0
    links = []
    while True:
        resp = requests.get(URL_NOTICIES+str(page))
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        tds = soup.find_all('td')
        page_links = [td.find('a',class_='state-published') for td in tds]
        if len(page_links) == 0:
            break
        [links.append(link) for link in page_links if link!=None]
        page+=JUMP
    return links

def get_notice_informations(notice:Notice) -> None:
        resp = requests.get(notice.url)
        soup = bs4.BeautifulSoup(resp.content, 'html.parser')
        notice.update_notice(soup)

if __name__ == '__main__':
    find_all_noticies()