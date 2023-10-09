import sys
sys.path.append("/home/hooniegit/git/organization/hawk-lake/api/lib")
from spotify import *


def thread_single():
    from time import time
    start_time = time()

    print("START THREAD >>>>>>>>>>")
    response = get_response(cnt=1, endpoint='albums', id='4aawyAB9vmqN3uQ7FjRGTy', params={'market' : 'KR'})
    print("FINISH THREAD <<<<<<<<<<")

    end_time = time()
    print(end_time - start_time)


def thread_all(cnt):
    from threading import Thread

    threads = []
    for cnt in range(0, cnt):
        thread = Thread(target=thread_single)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


def thread_single_duration(duration):
    from time import time, sleep
    start_time = time()

    print("START THREAD >>>>>>>>>>")
    response = get_response(cnt=1, endpoint='albums', id='4aawyAB9vmqN3uQ7FjRGTy', params={'market' : 'KR'})
    print("FINISH THREAD <<<<<<<<<<")

    end_time = time()
    sleep_time = duration - (end_time - start_time)
    sleep(sleep_time)


while True:
    # thread_single()
    # thread_single(duration=0.3)

    thread_all(20)