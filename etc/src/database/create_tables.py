import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../../../fastapi/lib')
sys.path.append(lib_dir)

from database import *


def drop_tables():
    conn = open_connector()

    query = f'''
    DROP TABLE IF EXISTS relations
    ''' # insert_date 자동 생성 제거
    cursor = conn.cursor()
    cursor.execute(query)

    query = f'''
    DROP TABLE IF EXISTS albums
    ''' # insert_date 자동 생성 제거
    cursor = conn.cursor()
    cursor.execute(query)

    query = f'''
    DROP TABLE IF EXISTS artists
    ''' # insert_date 자동 생성 제거
    cursor = conn.cursor()
    cursor.execute(query)

    conn.close()


def create_table_albums():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS albums(
        id INT AUTO_INCREMENT,
        album_id VARCHAR(30) PRIMARY KEY,
        release_date VARCHAR(10),
        insert_date DATE,
        UNIQUE KEY unique_column (id)
    )
    ''' # insert_date 자동 생성 제거
    cursor = conn.cursor()
    cursor.execute(query)

    conn.close()


def create_table_artists():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS artists(
        id INT AUTO_INCREMENT,
        artist_id VARCHAR(30) PRIMARY KEY,
        insert_date DATE,
        UNIQUE KEY unique_column (id)
    )
    ''' # insert_date 자동 생성
    cursor = conn.cursor()
    cursor.execute(query)

    conn.close()


def create_table_relations():
    conn = open_connector()
    query = f'''
    CREATE TABLE IF NOT EXISTS relations(
        album_id VARCHAR(30),
        artist_id VARCHAR(30),
        FOREIGN KEY (album_id) REFERENCES albums(album_id),
        FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
        UNIQUE KEY unique_combination (album_id, artist_id)
    )
    '''
    cursor = conn.cursor()
    cursor.execute(query)

    conn.close()


if __name__ == "__main__":
    drop_tables()
    create_table_albums()
    create_table_artists()
    create_table_relations()