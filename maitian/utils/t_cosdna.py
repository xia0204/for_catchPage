import requests
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(3)
cookie_s = {'lang': 'chs', 'PHPSESSID': 'ba4j8i6mp1be5vk86qnpjfe3l7'}
headers= {'Referer': 'http://www.cosdna.com/chs/product.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Host': 'www.cosdna.com'}
url = "http://www.cosdna.com/chs/product.php?q=%E5%B0%8F%E6%A3%95%E7%93%B6&p="
u = ['http://www.cosdna.com/chs/product.php?q=%E5%B0%8F%E6%A3%95%E7%93%B6&p=1', 'http://www.cosdna.com/chs/product.php?q=%E5%B0%8F%E6%A3%95%E7%93%B6&p=2', 'http://www.cosdna.com/chs/product.php?q=%E5%B0%8F%E6%A3%95%E7%93%B6&p=3', 'http://www.cosdna.com/chs/product.php?q=%E5%B0%8F%E6%A3%95%E7%93%B6&p=4']

def test0(url):
    return requests.get(url=url,headers=headers,cookies=cookie_s)

k = pool.map(test0,u)
[print(i.status_code) for i in list(k)]