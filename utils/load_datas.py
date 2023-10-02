import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, f'../lib')
sys.path.append(lib_dir)

from spotify import *
from datetime import datetime, timedelta

# 추후 source code의 양을 줄이기 위해 상단의 부분 등을 pip 모듈로 처리
# 상대 경로를 입력하면 sys.path.append를 자동으로 수행해주는 모듈 생성해보기

def browse_new_releases(cnt):

    endpoint = 'browse/new-releases'
    for cnt in range(0, 10):
        params = {
            'limit': '50',
            'offset': cnt * 50,
        }

    response = get_response(cnt=cnt, endpoint=endpoint, params=params)
    
    for item in response["albums"]["items"]:
        album_id = item["id"]
        input_date = datetime.now().strftime("%Y-%m-%d")
