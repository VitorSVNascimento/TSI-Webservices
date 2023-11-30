import requests
from models.notice import Notice
from constants import *
import bs4
import os
from concurrent.futures import ThreadPoolExecutor
from DAO import noticeDAO as dao
noticies = []

def find_all_noticies():
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