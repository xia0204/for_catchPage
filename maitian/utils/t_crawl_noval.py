# -*- coding: utf-8 -*-
import requests
import asyncio
import aiohttp
import gevent
import time
from bs4 import BeautifulSoup
from  multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
base_url = 'http://www.xbiquge.la'
test_url = 'http://www.xbiquge.la/13/13959/'

page_num  = 20

def test_1():
    res = requests.get(test_url, headers=header)
    res.encoding = 'utf8'
    text = res.text
    soup = BeautifulSoup(text, 'lxml')
    dd_list = soup.find_all('dd')
    dd_list0 = [i.find('a').get('href') for i in dd_list[:page_num]]
    for url in dd_list0:
        res = requests.get(base_url + url, headers=header)
        # print(res)


async def get(url,headers,session):
    await asyncio.sleep(0)
    content = session.get(url=url,headers=headers)
    return content

async def test_2():
    session = requests.session()
    res = session.get(test_url, headers=header)
    res.encoding = 'utf8'
    text = res.text
    soup = BeautifulSoup(text, 'lxml')
    dd_list = soup.find_all('dd')
    dd_list0 = [base_url+i.find('a').get('href') for i in dd_list[:page_num] ]
    await asyncio.gather(*[get(url, headers=header,session=session) for url in dd_list0])

                # print(res)


async def test_3():
    async with aiohttp.ClientSession() as session:
        async with session.get(test_url, headers=header) as res:
            res.encoding = 'utf8'
            text = await res.text()
            soup = BeautifulSoup(text, 'lxml')
            dd_list = soup.find_all('dd')
            dd_list0 = [i.find('a').get('href') for i in dd_list[:page_num]]
            for url in dd_list0:
                await session.get(base_url + url, headers=header)
        await asyncio.sleep(0.250)
                # print(res)
def get04(url,headers,session):
    # await asyncio.sleep(0)
    content = session.get(url=url,headers=headers)
    return content

def test_4():
    session = requests.session()
    res = session.get(test_url, headers=header)
    res.encoding = 'utf8'
    text = res.text
    soup = BeautifulSoup(text, 'lxml')
    dd_list = soup.find_all('dd')
    dd_list0 = [base_url+i.find('a').get('href') for i in dd_list[:page_num] ]
    # await asyncio.gather(*[get(url, headers=header,session=session) for url in dd_list0])
    gevent.joinall([gevent.spawn(get04,url,header,session) for url in dd_list0])

def run_common():
    start = time.time()
    test_1()
    end = time.time()

    print('requests所需时间', end - start)

def run_coroutine1():
    start1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_2())
    end1 = time.time()
    print('aiohttp我所需时间', end1 - start1)

def run_coroutine0():
    start1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_3())
    end1 = time.time()
    print('aiohttp原所需时间', end1 - start1)

def run_gevent():
    start1 = time.time()
    test_4()
    end1 = time.time()
    print('gevent原所需时间', end1 - start1)
if __name__ == '__main__':
    for i in range(5):
        p1 = Process(target=run_common)
        p2 = Process(target=run_coroutine0)
        p3 = Process(target=run_coroutine1)
        p4 = Process(target=run_gevent)

        p2.start()
        p3.start()
        p1.start()
        p4.start()
        p4.join()
        p1.join()
        p2.join()
        p3.join()
        print("\n")