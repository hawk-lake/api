import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
sys.path.append(lib_dir)

from spotify import *
from database import *

# 추후 source code의 양을 줄이기 위해 상단의 부분 등을 pip 모듈로 처리
# 상대 경로를 입력하면 sys.path.append를 자동으로 수행해주는 모듈 생성해보기

def browse_new_releases(cnt):
    endpoint = 'browse/new-releases'
    for page in range(0, 20):
        params = {
            'limit': '50',
            'offset': page * 50,
        }
        response = get_response(cnt=cnt, endpoint=endpoint, params=params)
        
        conn = open_connector()
        for item in response["albums"]["items"]:
            album_id = item["id"]
            release_date = item["release_date"]
            for artist in item["artists"]: 
                artist_id = artist["id"]
                query_artists = f'''
                                INSERT IGNORE INTO artists (id)
                                VALUES (%s);
                                '''
                values = (artist_id,)
                execute_query(conn, query_artists, values)
                print("comited : artists")
                
            values = (album_id, release_date)
            query_albums = f'''
                           INSERT IGNORE INTO albums (id, release_date)
                           values (%s, %s);
                           '''
            execute_query(conn, query_albums, (album_id, release_date))
            print("comited : albums")

        conn.close()

if __name__ == "__main__":
    browse_new_releases(3)