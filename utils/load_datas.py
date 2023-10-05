import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
data_dir = os.path.join(current_dir, f'../data')
sys.path.append(lib_dir)

from spotify import *
# from lib.spotify import *
from database import *


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


def browse_featured_playlists(cnt):
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")
    
    # spotify 발행 재생목록 '인기가요 Hot Now' 의 playlist_id 받아오기
    endpoint = 'browse/featured-playlists'
    params = {    
        'country' : 'KR',
        'locale' : 'en_KR',
        'timestamp' : f'{nowdate}T{nowtime}',
        'limit' : 1,
        'offset' : 0
    }
    response = get_response(cnt=cnt, endpoint=endpoint, params=params)
    playlist_id = response['playlists']['items'].pop()['id']

    # 위 재생목록의 트랙들의 앨범과 아티스트들 insert 하기
    endpoint = f'playlists/{playlist_id}/tracks'
    params = {
        'market' : 'KR',
        'fields' : 'items(track(album(id,release_date),artists(id)))',
        'limit' : 50,
        'offset' : 0
    }
    response = get_response(cnt=cnt, endpoint=endpoint, params=params)

    conn = open_connector()
    for item in response['items'] :
        album_id = item['track']['album']['id']
        release_date = item['track']['album']['release_date']
        for artist in item['track']['artists'] : 
            artist_id = artist['id']
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
    # browse_new_releases(3)
    browse_featured_playlists(1)
