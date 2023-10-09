import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../../lib')
sys.path.append(lib_dir)

from database import *


def create_table_albums():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS albums(
        id VARCHAR(30) PRIMARY KEY,
        release_date VARCHAR(10),
        insert_date DATE DEFAULT (CURRENT_DATE)
    );
    '''
    execute_query(conn, query)
    conn.close()


def create_table_artists():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS artists(
        id VARCHAR(30) PRIMARY KEY,
        insert_date DATE DEFAULT (CURRENT_DATE + INTERVAL 1 DAY)
    );
    '''
    execute_query(conn, query)
    conn.close()


def create_table_relations():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS relations(
        album_id VARCHAR(30),
        artist_id VARCHAR(30),
        FOREIGN KEY (album_id) REFERENCES albums(id),
        FOREIGN KEY (artist_id) REFERENCES artists(id)
    );
    '''
    execute_query(conn, query)
    conn.close()


if __name__ == "__main__":
    create_table_albums()
    create_table_artists()
    create_table_relations()