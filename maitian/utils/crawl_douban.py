from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from os import remove#删除文件
try:                                                                            #总体评价   豆瓣相对简单只存在一个验证码需要上传
    import cookielib
except:
    import http.cookiejar as cookielib
try:
    from PIL import Image
except:
    pass
url = "https://accounts.douban.com.login"
datas = {"source":"index_nav",
         "remember":"on",
         }

headers = {"Referer":"https://www.douban.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Language":"zh-CN,zh;q=0.8",
           }
session = requests.Session()
session.cookies = cookielib.LWPCookieJar(filename = "cookies")#从文件中加载cookie

try:
    session.cookies.load(ignore_discard=True)
except:
    print("未加载cookie")
    datas["form_email"] = "guoqi020@163.com"
    datas["form_password"] = "fghjkl"

def get_captcha():
    #获取验证码以及ID
    r = requests.post(url,data=datas,headers=headers)
    page = r.text
    soup = BeautifulSoup(page,"html.parser")
    #采用bs4获取验证码图片地址
    img_src= soup.find("img",{"id":"captcha_image"}).get("src")
    urlretrieve(img_src,"captcha.jpg")
    try:
        im = Image.open("captcha.jpg")
    except:
        print("手动打开查看")
    finally:
        captcha = input("please input caotcha code:")
        remove("captcha.jpg")
        captcha_id = soup.find("input",{"type":"hidden","name":"captcha-id"}).get("value")
        return captcha,captcha_id
def is_login():
    #通过查看个人账户信息来确认是否已经登录
    url = "https://www.douban.com/accounts"
    login_code = session.get(url,headers=headers,allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False
def login():
    captcha,captcha_id = get_captcha()
    #增加表数据
    datas["captcha-solution"]  = captcha
    datas["captcha-id"] = captcha_id
    login_page = session.post(url,data=datas,headers=headers)
    page = login_page.text
    soup = BeautifulSoup(page,"html.parser")
    result = soup.findAll("div",attrs={"class":"title"})
    #进入豆瓣登录后页面  打开热门内容
    for i in result:
        print(i.find("a").get_text())
    #保存cookie到本地
    #下次使用cookie登录
    session.cookies.save
if __name__ == "__main__":
    if is_login():
        print("login success")
    else:
        login()











