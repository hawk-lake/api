from fastapi import APIRouter, Request
from utils.load_datas import browse_featured_playlists

router = APIRouter()

@router.get("/mysql/both/featured_playlists")
async def get_browse_featured_playlists(cnt):
	return browse_featured_playlists(cnt)