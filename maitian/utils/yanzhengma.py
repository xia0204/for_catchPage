import PIL
import json
import requests as req
import brotli
from lxml import etree
import gevent
import os
import re
from gevent  import monkey
monkey.patch_all()
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
          "referer":"https://ivoting.chinatimes.com/succes/20191023001892-261001",
          "authority":"ivoting.chinatimes.com",
            "content-type": "application/x-www-form-urlencoded",
            "origin":"https://ivoting.chinatimes.com",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "path":"/succes/20191023001892-261001",
          }
header_img = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
          "referer":"https://ivoting.chinatimes.com/succes/20191023001892-261001",
          "authority":"ivoting.chinatimes.com",
            "content-type": "application/x-www-form-urlencoded",
            "origin":"https://ivoting.chinatimes.com",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "path":"/DefaultCaptcha/Refresh",
            "content-type": "application/x-www-form-urlencoded"
          }
header_img_get = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
          "referer":"https://ivoting.chinatimes.com/succes/20191023001892-261001",
          "authority":"ivoting.chinatimes.com",
            "content-type": "application/x-www-form-urlencoded",
            "origin":"https://ivoting.chinatimes.com",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "path":"/DefaultCaptcha/Generate?t=dabe56597d784468abc1432b5162e02e",
            "accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "content-type": "application/x-www-form-urlencoded"
          }
url = "http://my.cnki.net/Register/CheckCode.aspx?id=1541251235676"
url_chinatimes = "https://ivoting.chinatimes.com/DefaultCaptcha/Refresh"
cookie = "__cfduid=de88a60b94fbcbe53f6b296b17af930941571834099; ID=b47729d8-35f8-350e-32cf-fca774ccc0de; LDay=2019/10/23; AviviD_uuid=c907d1f4-61d2-4c82-a167-4e94e4b1d70d; webuserid=b1e241ba-2c19-1194-cec0-cbe873d629db; __gads=ID=8ab77ce3b1e08deb:T=1571834113:S=ALNI_Mbz8UCN1sV8zoRbe_7uVeHaUyyDsQ; vpadn-ctid=b4971947-f923-2740-98a4-bd65ab3c3dfd; vpadn-seid=vp24115010509-15718341145; vpadn-ce=1; vpadn-vpid=b4971947-f923-2740-98a4-bd65ab3c3dfd; _ga=GA1.2.762819149.1571834113; _gid=GA1.2.1323531660.1571834122; vpadn-sd=1571834135206; _huid=b27206c1-4a4d-4d79-b240-b3bb70ecacad; adid=b27206c1-4a4d-4d79-b240-b3bb70ecacad; ASP.NET_SessionId=yqvd3b1qxl04hhwvmam2eax3; Count=2; _ga=GA1.3.762819149.1571834113; _gid=GA1.3.1323531660.1571834122; oid=%257B%2522oid%2522%253A%252299e47c63-f591-11e9-97ef-0242ac120003%2522%252C%2522ts%2522%253A1571834131%252C%2522v%2522%253A%25221.0%2522%257D; _td=30fb3bd0-d47c-4cc3-a085-b0b40341e819"
# cookie = "__cfduid=de88a60b94fbcbe53f6b296b17af930941571834099; ID=b47729d8-35f8-350e-32cf-fca774ccc0de; AviviD_uuid=c907d1f4-61d2-4c82-a167-4e94e4b1d70d; webuserid=b1e241ba-2c19-1194-cec0-cbe873d629db; __gads=ID=8ab77ce3b1e08deb:T=1571834113:S=ALNI_Mbz8UCN1sV8zoRbe_7uVeHaUyyDsQ; vpadn-ctid=b4971947-f923-2740-98a4-bd65ab3c3dfd; vpadn-ce=1; vpadn-vpid=b4971947-f923-2740-98a4-bd65ab3c3dfd; _ga=GA1.2.762819149.1571834113; _gid=GA1.2.1323531660.1571834122; vpadn-sd=1571834135206; _huid=b27206c1-4a4d-4d79-b240-b3bb70ecacad; adid=b27206c1-4a4d-4d79-b240-b3bb70ecacad; ASP.NET_SessionId=yqvd3b1qxl04hhwvmam2eax3; _ga=GA1.3.762819149.1571834113; _gid=GA1.3.1323531660.1571834122; oid=%257B%2522oid%2522%253A%252299e47c63-f591-11e9-97ef-0242ac120003%2522%252C%2522ts%2522%253A1571834131%252C%2522v%2522%253A%25221.0%2522%257D; Count=3; Sended=Y; vpadn-seid=vp24115010509-15718475407; LDay=2019/10/24; _td=30fb3bd0-d47c-4cc3-a085-b0b40341e819; _hjid=5aaf9354-93e9-42d3-929e-699f37f5c8bd"
# data = {"t":"1055819fdf20446ab1572700d861ac29"} #a7e33f292bb54c858f14af8b3eba7f1a
data1 = {"Options":"","OptionsCheck":14557,"Options":"","Options":"","CurrentVoteStep": 0}
def test(cookie_str,data1,num):
    session = req.Session()
    cookie = {i.split("=")[0]:i.split("=")[1] for i in cookie_str.split("; ")}
    print(cookie)
    k = session.post(url = "https://ivoting.chinatimes.com/succes/20191023001892-261001",data=data1,headers = header,cookies=cookie)
    page = brotli.decompress(k.content)#br 压缩suanfa
    tree = etree.HTML(page.decode("utf-8"))#获取新图片名称
    t_code = tree.xpath('//input[@id="CaptchaDeText"]/@value')[0]
    print(t_code)
    img_url = "https://ivoting.chinatimes.com/DefaultCaptcha/Generate?t="+t_code
    print(img_url)
    img = session.get(img_url,headers=header_img_get)
    for i in range(50):
        print(i)
        if int(img.headers["Content-Length"]) < 1500:
            img = req.get(img_url, headers=header_img_get,cookies=cookie)
        else:
            with open("D:/checkcodeimg/chinatimes/code{}.gif".format(num), "wb") as f:
                f.write(img.content)
            break

if __name__ == "__main__":
    code_name_l = os.listdir("D:/checkcodeimg/chinatimes/")
    num_l = [int(re.match("code(\d{1,3}).*", i).groups()[0]) for i in code_name_l] #获取所有已经使用的数字
    now_num = max(num_l)

    g_list = [gevent.spawn(test(cookie_str=cookie,data1=data1,num=i)) for i in range(now_num,now_num+30)]
    gevent.joinall(g_list)
