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