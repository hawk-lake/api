def get_acccess_token(cnt):
    import os
    from configparser import ConfigParser

    # config.ini 파일 절대경로 반환
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(current_dir, f'../config/config.ini')

    # token 반환
    parser = ConfigParser()
    parser.read(config_dir)
    access_token = parser.get("SPOTIFY", f"access_token_{cnt}")
    return access_token


def get_response(cnt, endpoint, params:dict=None):
    import os, sys, requests
    from datetime import datetime

    # 현재 날짜 및 시간 반환
    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    # error 파일 절대경로 반환
    current_dir = os.path.dirname(os.path.abspath(__file__))
    error_dir = os.path.join(current_dir, f'../log/request/error/{nowdate}.error')

    # request 요청 용 파라미터 생성
    access_token = get_acccess_token(cnt)
    url = f"https://api.spotify.com/v1/{endpoint}"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    print(url)

    # request 요청
    if params != None:
        response = requests.get(url=url, params=params, headers=headers)
        print(response)
    else:
        response = requests.get(url=url, headers=headers)

    # 오류 제어 / 오류 발생 시 프로그램 종료
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        error = f"KEY-{cnt}: ERROR APPEARED: {nowtime}: {response.status_code} \n"
        try:
            with open(error_dir, "a") as file:
                file.write(error)
        except:
            with open(error_dir, "w") as file:
                file.write(error)      
        print("ERROR APEEARED")      
        sys.exit()


# TEST
if __name__ == "__main__":

    # # albums : 단일 앨범 response
    # id='4aawyAB9vmqN3uQ7FjRGTy'
    # endpoint=f'albums/{id}'
    # params={'market' : 'KR'}

    # # albums tracks : 단일 앨범 / 다중 트랙 response
    # id = '4aawyAB9vmqN3uQ7FjRGTy'
    # endpoint = f'albums/{id}/tracks'
    # params = {
    #     'market' : 'KR',
    #     'limit': '50',
    #     'offset': '0',
    # }

    # new_release : 다중 앨범 response
    endpoint = 'browse/new-releases'
    params = {
        'limit': '50',
        'offset': '0',
    }
    response = get_response(cnt=3, endpoint=endpoint, params=params)

    # # artists : 단일 아티스트 response
    # id = '0TnOYISbd1XYRBk9myaseg'
    # endpoint = f'artists/{id}'
    # response = get_response(cnt=3, endpoint=endpoint)

    # # artists albums : 단일 아티스트 / 다중 앨범 response
    # id = '0TnOYISbd1XYRBk9myaseg'
    # endpoint = f'artists/{id}/albums'
    # response = get_response(cnt=1, endpoint=endpoint)

    # # artists related artists : 단일 아티스트 / 다중 아티스트 response
    # id = '0TnOYISbd1XYRBk9myaseg'
    # endpoint = f'artists/{id}/related-artists'
    # response = get_response(cnt=1, endpoint=endpoint)

    print(response)


''' 23-10-02
엔드포인트 구조 수정 사유
/endpoint/id?params 구조인 경우를 상정하고 코드 작성
/endpoint/id/endpoint 구조를 발견하여 수정
'''
