# spotify-api (v1.0.0)

## Features

### 1. spotify api - access token 업데이트
```
.
├── config
│   └── config.ini
├── sh
│   └── cron.sh
├── src
│   └── cron
│       └── change_access_key.py
└── log
    └── cron.log
```

### 2. spotify api - request와 response 규격화
```
├── lib
│   └── spotify.py
└── log
    └── request
        └── error
            ├── 2023-10-01.error
            ├── ...
            └── 2023-10-05.error
```

### 3. album, artist 데이터 -> db 및 json 적재
```
├── lib
│   ├── database.py
│   └── files.py
├── src
│   └── database
│       └── create_tables.py
├── utils
│    └── load_datas.py
└── data
    ├── albums
    │   ├── 2023-10-03
    │   │   ├── 0TPSnNtb4boimpeYCN5XFq.json
    │   │   ├── ...
    │   │   └── 7vQRJ5q9b0c4gKrsh9yIhE.json
    │   └── 2023-10-05
    │       ├── 0cuXDMN1yjtTrYJfrnVxFq.json
    │       ├── ...
    │       └── 7yXtdZLKdtwH5FrxduK7ti.json
    ├── bin
    └── tracks
        ├── 2023-10-03
        │   ├── 00syWkRGIVQvYsg2OwfBUw.json
        │   ├── ...
        │   └── 7zhh7c8HQwMx97SKAgJqOn.json
        └── 2023-10-05
            ├── 00XrbymEYDhTSLwsWTzxor.json
            ├── ...
            └── 7xcVfRQTIwTQrDJN29llIx.json
```

### 4. fast api 엔드포인트 라우팅 및 서버 실행

* 엔드포인트 요약
  * /mysql/both/new_release
  * /mysql/both/featured_playlists
  * /mysql/artists/related_artists
  * /mysql/album/artist_albums
  * /json/albums
  * /json/artists

```
├── main.py
└── router
    └── load_data.py
```

## Overall Tree
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