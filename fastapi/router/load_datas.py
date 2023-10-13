from fastapi import APIRouter
from utils.load_datas import *

router = APIRouter()

# [1]
@router.get("/mysql/both/new_release")
async def get_browse_new_releases(cnt:int):
	return browse_new_releases(cnt)

# [2]
@router.get("/mysql/both/featured_playlists")
async def get_browse_featured_playlists(cnt:int):
	return browse_featured_playlists(cnt)

# [3]
@router.get("/mysql/artists/related_artists")
async def get_artists_related_artists(cnt:int, insert_date:str):
	return artists_related_artists(cnt, insert_date)

# [4]
@router.get("/mysql/album/artist_albums")
async def get_artists_albums(insert_date:str):
	return thread_artists_albums(insert_date)

# [5]
@router.get("/json/albums")
async def get_albums(insert_date:str):
	return thread_albums(insert_date)

# [6]
@router.get("/json/artists")
async def get_artists(insert_date:str):
	return thread_artists(insert_date)

"""
1. [1], [2] 같은 시간에 동시 실행 / 별도의 키 사용
2. [3] 실행 / 단일 키 사용
3. [4] 실행
4. [5] 실행
5. [6] 실행
6. [7], [8], [9] 같은 시간에 동시 실행
"""