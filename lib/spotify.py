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


def get_response(cnt, endpoint, id, params:dict):
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
    url = f"https://api.spotify.com/v1/{endpoint}/{id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # request 요청
    response = requests.get(url=url, params=params, headers=headers)

    # 오류 제어 / 오류 발생 시 프로그램 종료
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        error = f"ERROR APPEARED : {nowtime} : {response.status_code} \n"
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
    response = get_response(cnt=1, endpoint='albums', id='4aawyAB9vmqN3uQ7FjRGTy', params={'market' : 'KR'})
    print(response)