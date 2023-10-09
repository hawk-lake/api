# About
- Fast API 서버로 구축한 데이터 수집 파이프라인입니다.
- Spotify API 를 이용해 artist와 album 데이터를 수집합니다.

# Structure
- 

# Get Started
## Mysql 서버 준비사항
1. 설치한 mysql에 맞춰 `lib/database.py` 에서 connection 정보 수정
2. 테이블 생성 스크립트 실행
```
python3 src/database/create_tables.py
```

## Fast API 서버 준비사항
1. Fast API 서버 실행에 필요한 모듈 설치
```
pip install uvicorn fastapi 
```
2. Fast API 서버 실행 (8000 포트 기존 사용시, 다른 포트로 변경)
```
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```
3. 각 엔드포인트 테스트
`https://localhost:8000/docs` 스웨거 ui 이용해 엔드포인트 테스트 출력해보기
* - /mysql/both/new_release
- /mysql/both/featured_playlists
- /mysql/artists/related_artists
- /mysql/album/artist_albums
- /json/albums
- /json/artists


# Tree
```
.
├── README.md
├── config
│   └── config.ini
├── data
│   ├── albums
│   │   ├── 2023-10-03
│   │   │   ├── 0TPSnNtb4boimpeYCN5XFq.json
│   │   │   ├── ...
│   │   │   └── 7vQRJ5q9b0c4gKrsh9yIhE.json
│   │   └── 2023-10-05
│   │       ├── 0cuXDMN1yjtTrYJfrnVxFq.json
│   │       ├── ...
│   │       └── 7yXtdZLKdtwH5FrxduK7ti.json
│   ├── bin
│   └── tracks
│       ├── 2023-10-03
│       │   ├── 00syWkRGIVQvYsg2OwfBUw.json
│       │   ├── ...
│       │   └── 7zhh7c8HQwMx97SKAgJqOn.json
│       └── 2023-10-05
│           ├── 00XrbymEYDhTSLwsWTzxor.json
│           ├── ...
│           └── 7xcVfRQTIwTQrDJN29llIx.json
├── demo
│   └── check_limit.py
├── lib
│   ├── database.py
│   ├── files.py
│   └── spotify.py
├── log
│   ├── cron.log
│   └── request
│       └── error
│           ├── 2023-10-01.error
│           ├── ...
│           └── 2023-10-05.error
├── main.py
├── router
│   ├── bin
│   └── load_data.py
├── sh
│   └── cron.sh
├── src
│   ├── cron
│   │   └── change_access_key.py
│   └── database
│       └── create_tables.py
└── utils
    └── load_datas.py
```

# Notice
* 