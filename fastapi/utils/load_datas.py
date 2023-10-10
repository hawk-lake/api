import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
data_dir = os.path.join(current_dir, f'../datas')
sys.path.append(lib_dir)

from spotify import *
from database import *


# confirmed: 23.10.10
def browse_new_releases(cnt):
    from time import time, sleep
    from datetime import datetime

    insert_date = datetime.now().strftime("%Y-%m-%d")

    # request & response
    endpoint = 'browse/new-releases'
    for page in range(0, 20):
        params = {
            'limit': '50',
            'offset': page * 50,
        }

        start_time = time()

        response = get_response(cnt=cnt, endpoint=endpoint, params=params)
        
        # open conn
        conn = open_connector()

        for item in response["albums"]["items"]:
            album_id = item["id"]
            release_date = item["release_date"]

            # MySQL: albums
            query_albums = f'''
                           INSERT IGNORE INTO albums (album_id, release_date, insert_date)
                           values (%s, %s, %s)
                           '''
            values = (album_id, release_date, insert_date)
            execute_query(conn, query_albums, values)

            for artist in item["artists"]: 
                artist_id = artist["id"]

                # MySQL: artists
                query_artists = f'''
                                INSERT IGNORE INTO artists (artist_id, insert_date)
                                VALUES (%s, %s)
                                '''
                values = (artist_id, insert_date)
                execute_query(conn, query_artists, values)

                # MySQL: relations
                query_relations = f'''
                                INSERT IGNORE INTO relations (album_id, artist_id)
                                VALUES (%s, %s)
                                '''
                values = (album_id, artist_id)
                execute_query(conn, query_relations, values)

        end_time = time()
        remain_time = 1 - (end_time - start_time)
        sleep(remain_time)      

        # close conn
        conn.close()


# confirmed: 23.10.10
def browse_featured_playlists(cnt):
    from time import time, sleep
    from datetime import datetime

    insert_date = datetime.now().strftime("%Y-%m-%d")
    insert_time = datetime.now().strftime("%H:%M:%S")
    
    # request & response
    endpoint = 'browse/featured-playlists'
    params = {    
        'country' : 'KR',
        'locale' : 'en_KR',
        'timestamp' : f'{insert_date}T{insert_time}',
        'limit' : 1,
        'offset' : 0
    }

    start_time = time()

    response = get_response(cnt=cnt, endpoint=endpoint, params=params)

    end_time = time()
    remain_time = 1 - (end_time - start_time)
    sleep(remain_time)      

    # request & response
    playlist_id = response['playlists']['items'].pop()['id']
    endpoint = f'playlists/{playlist_id}/tracks'
    params = {
        'market' : 'KR',
        'fields' : 'items(track(album(id,release_date),artists(id)))',
        'limit' : 50,
        'offset' : 0
    }

    start_time = time()
    response = get_response(cnt=cnt, endpoint=endpoint, params=params)

    # open conn
    conn = open_connector()

    for item in response['items'] :
        album_id = item['track']['album']['id']
        release_date = item['track']['album']['release_date']

        # MySQL: albums
        query_albums = f'''
                        INSERT IGNORE INTO albums (album_id, release_date, insert_date)
                        values (%s, %s, %s)
                        '''
        values = (album_id, release_date, insert_date)
        execute_query(conn, query_albums, values)

        for artist in item['track']['artists'] : 
            artist_id = artist['id']

            # MySQL: artists
            query_artists = f'''
                                INSERT IGNORE INTO artists (artist_id, insert_date)
                                VALUES (%s, %s)
                                '''
            values = (artist_id, insert_date)
            execute_query(conn, query_artists, values)

            # MySQL: relations
            query_artists = f'''
                                INSERT IGNORE INTO relations (album_id, artist_id)
                                VALUES (%s, %s)
                                '''
            values = (album_id, artist_id)
            execute_query(conn, query_artists, values)

    end_time = time()
    remain_time = 1 - (end_time - start_time)
    sleep(remain_time)   

    # close conn
    conn.close()


# confirmed: 23.10.10
def artists_related_artists(cnt, insert_date):
    from time import time, sleep

    # open conn
    conn = open_connector()

    # create id list
    query_search = f"""
                   SELECT artist_id FROM artists
                   WHERE insert_date = '{insert_date}'
                   """
    result = fetchall_query(conn=conn, query=query_search)
    id_list = [artist[0] for artist in result]

    for artist_id in id_list:
        endpoint = f'artists/{artist_id}/related-artists'

        start_time = time()

        response = get_response(cnt=cnt, endpoint=endpoint)
        for related_artist in response['artists']:
            related_artist_id = related_artist['id']
            query_artists = f'''
                            INSERT IGNORE INTO artists (artist_id, insert_date)
                            VALUES (%s, %s)
                            '''
            values = (related_artist_id, insert_date)
            execute_query(conn, query_artists, values)

        end_time = time()
        remain_time = 1 - (end_time - start_time)
        sleep(remain_time)      

    # close conn
    conn.close()


# confirmed: 23.10.10
def artists_albums(cnt, insert_date):
    from time import time, sleep

    # open conn
    conn = open_connector()

    # make id list
    query_search = f"""
                   SELECT artist_id FROM artists
                   WHERE insert_date = '{insert_date}'
                   """
    result = fetchall_query(conn=conn, query=query_search)
    id_list = [artist[0] for artist in result]

    for artist_id in id_list:
        # request & response
        endpoint = f'artists/{artist_id}/albums'

        start_time = time()

        response = get_response(cnt=cnt, endpoint=endpoint)

        for album in response['items']:
            album_id = album['id']
            release_date = album['release_date']

            # MySQL: albums
            query_albums = f'''
                            INSERT IGNORE INTO albums (album_id, release_date, insert_date)
                            VALUES (%s, %s, %s)
                            '''
            values = (album_id, release_date, insert_date)
            execute_query(conn, query_albums, values)

            # MySQL: relations
            query_relations = f'''
                            INSERT IGNORE INTO relations (album_id, artist_id)
                            VALUES (%s, %s)
                            '''
            values = (album_id, artist_id)
            execute_query(conn, query_relations, values)

        end_time = time()
        remain_time = 1 - (end_time - start_time)
        sleep(remain_time)             

    # close conn
    conn.close()


# 
def albums(cnt, insert_date):
    from time import time, sleep
    from files import file_json

    # open conn
    conn = open_connector()

    # create path
    try: os.makedirs(f"{data_dir}/albums/{insert_date}")
    except: pass
    try: os.makedirs(f"{data_dir}/tracks/{insert_date}")
    except: pass

    # create id list
    query_search = f"""
                   SELECT album_id FROM albums
                   WHERE insert_date = '{insert_date}'
                   """
    result = fetchall_query(conn=conn, query=query_search)
    id_list = [album[0] for album in result]

    # close conn
    conn.close()

    for album_id in id_list:
        # request & response
        endpoint=f'albums/{album_id}'
        params={'market' : 'KR'}

        start_time = time()

        response = get_response(cnt=cnt, endpoint=endpoint, params=params)

        # save file
        file_dir = f"{data_dir}/albums/{insert_date}/{album_id}.json"
        file_json(file_dir=file_dir, json_data=response)

        for track in response['tracks']['items']:
             track_id = track["id"]

             # save file
             file_dir = f"{data_dir}/tracks/{insert_date}/{track_id}.json"
             file_json(file_dir=file_dir, json_data=track)

        end_time = time()
        remain_time = 1 - (end_time - start_time)
        sleep(remain_time)      


def artists(cnt, insert_date):
    from time import time, sleep
    from files import file_json

    conn = open_connector()
    try: os.makedirs(f"{data_dir}/artists/{insert_date}")
    except: pass

    query_search = f"""
                   SELECT artist_id FROM artists
                   WHERE insert_date = '{insert_date}'
                   """
    result = fetchall_query(conn=conn, query=query_search)
    conn.close()

    id_list = [artist[0] for artist in result]
    for id in id_list:
        endpoint = f'artists/{id}'
        params = {'market' : 'KR'}

        start_time = time()

        response = get_response(cnt=cnt, endpoint=endpoint, params=params)
        file_dir = f"{data_dir}/artists/{insert_date}/{id}.json"
        file_json(file_dir=file_dir, json_data=response)

        end_time = time()
        remain_time = 1 - (end_time - start_time)
        sleep(remain_time)


if __name__ == "__main__":
    # browse_new_releases(1)
    # browse_featured_playlists(1)

    date = "2023-10-10"
    artists_related_artists(2, date)
    # artists_albums(1, date)
    # albums(1, date)
    # artists(2, date)