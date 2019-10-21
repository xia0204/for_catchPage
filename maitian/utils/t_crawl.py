import gevent
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
1、 首先找到文件的下载链接   通过文件大小找到文件  找到下载链接
2、 分析下载链接  分析多个下载链接中参数变化  发现文件名字在变    vkey在变
3、 songmid在页面中  然后需要寻找vkey  可以在开发者组件中查询vkey 可以找到  但是多个链接中只有少个可以使用
        多数情况下无法直接查询所有响应中的东西  开发一个东西在所有的响应中查询东西  
4、 过滤url找到vkey的请求网址是什么   然后构造vkey的请求网址        
"""
"""
import requests#爬虫登录马蜂窝
from lxml import etree
session = requests.Session()#使用session
phone_num = ""
password = ""#账户密码
data = {"passport":phone_num,"password":password}
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                }#构造头
login = session.post("https://passport.mafengwo.cn/login",headers=headers,data=data)#登录链接
print(login.status_code)

login_url = "http://www.mafengwo.cn/friend/index/follow?uid=70360114"#获得cookie后登陆
response = session.get(login_url,headers=headers)
tree = etree.HTML(response.text)#解析
friend = tree.xpath("")#解析数据
print(friend)
"""


"""
import requests
# http://127.0.0.1:61000/j_acegi_security_check
url = "http://127.0.0.1:61000/j_acegi_security_check"
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",        
                }
data = {"j_username":"test","j_password":"111111",headers=headers}
login_jekins = requests.post(url,data=data)
print(login_jekins.text)#爬虫爬取jekins登录
"""

#github
import requests#爬虫登录github
from lxml import etree

class Login():
    def __init__(self):
        self.headers = {
            "Referer":"https://github.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "Host":"github.com"
            }
        self.login_url = "https://github.com/login"
        self.post_url = "https://github.com/session"
        self.logined_url_url = "https://github.com/settings/profile"
        self.session = requests.Session()
    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath("//div//input[2]/@value")[0]
        print("authenticity_token = ",token)
        return token
    def login(self,email,password):
        post_data = {
            "commit":"Sign in",
            "utf8":"✔",
            "authenticity_token":self.token(),
            "login":email,
            "password":password,
        }
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        print("login status code:",response.status_code)
        print(response.cookies.get_dict())
        print(response.request.headers)
        if response.status_code == 200:
            self.repositories_name(response.text)
        response = self.session.get(self.login_url,headers=self.headers)
        print("profile status code:",response.status_code)
        if response.status_code == 200:
            self.logo(response.text)

    def repositories_name(self,html):
        selector = etree.HTML(html)
        repositories_name = selector.xpath('//li[contains(@class,"public source")]/div/[@class="width-f..."]')
        print(repositories_name)
    def logo(self,html):
        selector = etree.HTML(html)
        logo_url = selector.xpath('//dl[contains(@class,"form-group")]//dd/img/@src')[0]
        print("logo url :",logo_url)

login = Login()
login.login(email="guoqi020@163.com",password="testdevops123.0")

""""""""""""#cookie 切割复用
"""
cookie_str = "_ga=GA1.2.2025357332.1503554449; _device_id=8fd51d87d009b95c7271fef8379dfe33; _octo=GH1.1.868824807.1566757246; user_session=d7FCyMBzXKblixZjp2Gkkqlt_-EkSo8CQYTQVUFjTrAp-ZeR; __Host-user_session_same_site=d7FCyMBzXKblixZjp2Gkkqlt_-EkSo8CQYTQVUFjTrAp-ZeR; logged_in=yes; dotcom_user=xia0204; has_recent_activity=1; _gh_sess=SURMY0ZXaHNpMkg1OGdVRXM1WlRteW5qZmt3Q01YbmpkUG9RamFEbkV3QWNwajVQMXlSTEFBNDN6aGJGTVh4UnBYU0pMNHJ4QWxTZkxDZGtyaTltRHc9PS0teWxQOUlPTHh6dHBlbmU0U24vUmJiZz09--e1d77ddb31b6a865c83c92da780c954c4a08d1cd"

cookie_l0 = cookie_str.split("; ")
cd = {}
for i in cookie_l0:
     k = i.split("=")
     cd[k[0]] = k[1]
     """
""""""""""""#cookie 切割复用
