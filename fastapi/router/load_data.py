from fastapi import APIRouter
from utils.load_datas import *

router = APIRouter()

@router.get("/mysql/both/new_release")
async def get_browse_new_releases(cnt:int):
	return browse_new_releases(cnt)

@router.get("/json/albums")
async def get_albums(cnt:int):
	return albums(cnt)

@router.get("/json/artists")
async def get_artists(cnt:int):
	return artists(cnt)

@router.get("/mysql/album/artist_albums")
async def get_artists_albums(cnt:int):
	return artists_albums(cnt)

@router.get("/mysql/artists/related_artists")
async def get_artists_related_artists(cnt:int):
	return artists_related_artists(cnt)

@router.get("/mysql/both/featured_playlists")
async def get_browse_featured_playlists(cnt:int):
	return browse_featured_playlists(cnt)
