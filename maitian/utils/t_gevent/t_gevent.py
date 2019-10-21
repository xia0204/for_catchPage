import gevent
from gevent import monkey,Greenlet
import requests
import time
import multiprocessing
gevent.monkey.patch_all()
# def test0():
#     print(1)
#     gevent.sleep(0)
#     print(2)
#
# def test1():
#     print(3)
#     gevent.sleep(0)
#     time.sleep(0.1)
#     print(4)

def get_img():
    gevent.sleep(0)
    requests.get("http://my.cnki.net/Register/CheckCode.aspx?id=1541251235676")


def get_img_re():
    s_time = time.time()
    for i in range(20):
        a = requests.get("http://my.cnki.net/Register/CheckCode.aspx?id=1541251235676")
        # print(i)
    l_time = time.time() - s_time
    print("re time:",l_time)
def get_img_ge():
    s_time = time.time()
    li = [gevent.spawn(get_img) for i in range(5)]
    gevent.joinall(li)
    l_time = time.time() - s_time
    print("ge time:",l_time)
if __name__== "__main__":
    for i in range(5):
        p1 = multiprocessing.Process(target=get_img_re)
        p2 = multiprocessing.Process(target=get_img_ge)
        p1.start()
        p2.start()
        p1.join()
        p2.join()

