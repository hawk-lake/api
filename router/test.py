from fastapi import APIRouter, Request
from utils.load_datas import *

router = APIRouter()

@router.get("/mysql/both/featured_playlists")
async def browse_featured_playlists(cnt):
	return browse_featured_playlists(cnt)