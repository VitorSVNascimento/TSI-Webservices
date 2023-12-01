import sqlite3
from models.notice import Notice

DATABASE_NAME = 'database/noticeifsudeste.db'
def create_table():
    cnn = sqlite3.connect(DATABASE_NAME)
    cursor = cnn.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS notice (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    url TEXT,
    year TEXT,
    number TEXT,
    situation TEXT,
    modality TEXT,
    pdf_link TEXT
);
    ''')

    cnn.commit()
    cnn.close()

def insert(notice:Notice):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Inserção de uma notícia na tabela
    cursor.execute('''
       INSERT INTO notice (name, url, year, number, situation, modality, pdf_link)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    ''', (notice.name, notice.url,notice.year,notice.number,notice.situation,notice.modality,notice.pdf_link))

    conn.commit()
    conn.close()

def get_by_filters(year,modality,number,situation,terms):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = __make_sql_query(year,modality,number,situation,terms)
    print(query)
    cursor.execute(query)
    results = cursor.fetchall()
    # print('Results ', results)
    notice_list = [tuple_to_notice(result) for result in results]
    # print('Notice ', notice_list)
    return notice_list



def tuple_to_notice(data_tuple):
    return Notice(*data_tuple)

def __make_sql_query(year,modality,number,situation,terms):
    query = 'SELECT * FROM notice WHERE '
    for term in terms:
        query += f'LOWER(name) LIKE \'%{term.lower()}%\' '
        if term == terms[-1]:
            query += 'AND '
        else:
            query += 'OR '
    if year != None and len(year) == 0:
        query += f'year = {year} AND '
    if modality != None and len(modality) == 0:
        query += f'LOWER(modality) = {modality.lower()} AND '
    if number != None and len(number) == 0:
        query += f'number = {number} AND '
    if situation != None and len(situation) == 0:
        query += f'LOWER(situation) = {situation.lower()};'

    query = query.strip()
    if query.endswith('OR'):
        query = f'{query[:-3]};'
    elif query.endswith('AND'):
        query = f'{query[:-4]};'
    return query
    pass