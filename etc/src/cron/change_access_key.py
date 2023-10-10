import os, sys, requests
from configparser import ConfigParser

# cnt 반환
cnt = sys.argv[1]

# config.ini 파일 절대경로 반환
current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, f'../../../fastapi/config/config.ini')

# ConfigParser 인스턴스 생성
parser = ConfigParser()
parser.read(config_dir)

# token 발급 용 파라미터 반환
client_id = parser.get("SPOTIFY", f"client_id_{cnt}")
client_sc = parser.get("SPOTIFY", f"client_sc_{cnt}")

# token 발급 용 request 요청
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_sc}'.encode()
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data).json()

# token 데이터 추출
access_token = response['access_token']

# config.ini 데이터 수정
parser.set('SPOTIFY', f'access_token_{cnt}', access_token)
with open(config_dir, 'w') as configfile:
    parser.write(configfile)