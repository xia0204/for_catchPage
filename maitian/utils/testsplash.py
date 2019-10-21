import requests as req


import json
import requests

# 需要添加的请求头
headers = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                   ' (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'),
]

params = {
    'url': 'http://baidu.com',
    'http_method': 'GET',
    'headers': headers,
}

a = requests.post(url='http://localhost:8050/render.html',
              #headers={'Content-Type': 'text/html'},
              data=json.dumps(params))
print(a.text)