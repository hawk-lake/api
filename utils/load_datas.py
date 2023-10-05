import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
data_dir = os.path.join(current_dir, f'../data')
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


def albums(cnt):
    from datetime import datetime
    from files import file_json

    conn = open_connector()
    # nowdate = datetime.now().strftime("%Y-%m-%d")
    nowdate = "2023-10-03"
    try: os.makedirs(f"{data_dir}/albums/{nowdate}")
    except: pass
    try: os.makedirs(f"{data_dir}/tracks/{nowdate}")
    except: pass

    query_search = f"""
                   SELECT id FROM albums
                   WHERE insert_date = '{nowdate}';
                   """
    result = fetchall_query(conn=conn, query=query_search)
    conn.close()

    id_list = [album[0] for album in result]
    for id in id_list:
        endpoint=f'albums/{id}'
        params={'market' : 'KR'}
        response = get_response(cnt=cnt, endpoint=endpoint, params=params)
        file_dir = f"{data_dir}/albums/{nowdate}/{id}.json"
        file_json(file_dir=file_dir, json_data=response)

        for track in response['tracks']['items']:
             id = track["id"]
             file_dir = f"{data_dir}/tracks/{nowdate}/{id}.json"
             file_json(file_dir=file_dir, json_data=track)


def artists(cnt):
    from datetime import datetime
    from files import file_json

    conn = open_connector()
    nowdate = datetime.now().strftime("%Y-%m-%d")
    # nowdate = "2023-10-04"
    try: os.makedirs(f"{data_dir}/artists/{nowdate}")
    except: pass

    query_search = f"""
                   SELECT id FROM artists
                   WHERE insert_date = '{nowdate}';
                   """
    result = fetchall_query(conn=conn, query=query_search)
    conn.close()

    id_list = [artist[0] for artist in result]
    for id in id_list:
        endpoint=f'artists/{id}'
        params={'market' : 'KR'}
        response = get_response(cnt=cnt, endpoint=endpoint, params=params)
        file_dir = f"{data_dir}/artists/{nowdate}/{id}.json"

        file_json(file_dir=file_dir, json_data=response)


def artists_albums(cnt):
    from datetime import datetime

    conn = open_connector()
    nowdate = datetime.now().strftime("%Y-%m-%d")

    query_search = f"""
                   SELECT id FROM artists
                   WHERE insert_date = '{nowdate}';
                   """
    result = fetchall_query(conn=conn, query=query_search)
    conn.close()

    id_list = [artist[0] for artist in result]
    for id in id_list:
        endpoint = f'artists/{id}/related-artists'
        response = get_response(cnt=cnt, endpoint=endpoint)
        for artist in response['artists']:
                id = artist['id']
                query_artists = f'''
                                INSERT IGNORE INTO artists (id)
                                VALUES (%s);
                                '''
                values = (id,)
                execute_query(conn, query_artists, values)
                print("comited : artists")    


def artists_related_artists(cnt):
    from datetime import datetime

    conn = open_connector()
    nowdate = datetime.now().strftime("%Y-%m-%d")

    query_search = f"""
                   SELECT id FROM artists
                   WHERE insert_date = '{nowdate}';
                   """
    result = fetchall_query(conn=conn, query=query_search)
    conn.close()

    id_list = [artist[0] for artist in result]
    for id in id_list:
        endpoint = f'artists/{id}/related-artists'
        response = get_response(cnt=cnt, endpoint=endpoint)
        for artist in response['artists']:
                id = artist['id']
                query_artists = f'''
                                INSERT IGNORE INTO artists (id)
                                VALUES (%s);
                                '''
                values = (id,)
                execute_query(conn, query_artists, values)
                print("comited : artists")


if __name__ == "__main__":
    # browse_new_releases(2)
    # print("DONE")

    albums(2)
    print("DONE")

    # artists(2)
    # print("DONE")

    # artists_related_artists(2)
    # print("DONE")