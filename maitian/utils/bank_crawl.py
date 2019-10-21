import requests as req
from lxml import etree
import re
import json
import gevent
from gevent import  monkey
monkey.patch_all()

bank_url = ['/bank/402/', '/bank/103/', '/bank/102/', '/bank/105/', '/bank/313/', '/bank/104/', '/bank/403/', '/bank/301/', '/bank/314/', '/bank/203/', '/bank/401/', '/bank/317/', '/bank/308/', '/bank/302/', '/bank/309/', '/bank/320/', '/bank/303/', '/bank/310/', '/bank/305/', '/bank/306/', '/bank/304/', '/bank/307/', '/bank/322/', '/bank/313S/', '/bank/313B/', '/bank/319/', '/bank/989/', '/bank/315/', '/bank/502/', '/bank/907/', '/bank/316/', '/bank/318/', '/bank/969/', '/bank/321/', '/bank/201/', '/bank/501/', '/bank/781/', '/bank/202/', '/bank/906/', '/bank/787/', '/bank/504/', '/bank/593/', '/bank/671/', '/bank/595/', '/bank/597/', '/bank/564/', '/bank/596/', '/bank/503/', '/bank/531/', '/bank/561/', '/bank/621/', '/bank/691/', '/bank/623/', '/bank/533/', '/bank/563/', '/bank/510/', '/bank/712/', '/bank/661/', '/bank/591/', '/bank/514/', '/bank/782/', '/bank/903/', '/bank/717/', '/bank/631/', '/bank/505/', '/bank/562/', '/bank/506/', '/bank/532/', '/bank/786/', '/bank/752/', '/bank/761/', '/bank/771/', '/bank/901/', '/bank/783/', '/bank/692/', '/bank/652/', '/bank/592/', '/bank/616/', '/bank/713/', '/bank/622/', '/bank/902/', '/bank/633/', '/bank/693/', '/bank/785/', '/bank/641/', '/bank/594/', '/bank/904/', '/bank/682/', '/bank/509/', '/bank/507/', '/bank/908/', '/bank/909/', '/bank/534/', '/bank/565/', '/bank/651/', '/bank/512/', '/bank/694/', '/bank/695/', '/bank/711/', '/bank/681/', '/bank/714/', '/bank/715/', '/bank/716/', '/bank/513/', '/bank/732/', '/bank/741/', '/bank/742/', '/bank/751/', '/bank/672/', '/bank/662/', '/bank/775/', '/bank/776/', '/bank/905/']
baseurl = "http://www.5cm.cn"
headers ={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
patter = re.compile("^\.")

def do_get_bank_pro_pagenuml(url):
    full_bank_url = baseurl+url
    pageSource = req.get(full_bank_url,headers).text
    tree = etree.HTML(pageSource)#获取页面数据 格式化为lxml格式
    bank_name = tree.xpath('//div[@class="container"]/h1/text()')[0]#获取银行名称
    last_page_num = tree.xpath('//ul[@class="pagination"]/li[last()-1]/a/text()') #获取银行当前页数总和
    if len(last_page_num) == 0:#针对当前页没有碰到分页情况的
        last_page_num = 0
    elif patter.match(last_page_num[0]):#针对当前页是有分页且过长出现省略的
        last_page_num = last_page_num[0].split(" ")[1]
    else:#针对当前分页没有省略分页的
        last_page_num = last_page_num[0]
    print(url,bank_name,last_page_num)
    #可能存在只有三页但是没有下一页的情况


if __name__ == "__main__":
    gevent.joinall(
        [
            gevent.spawn(do_get_bank_pro_pagenuml,i) for i in bank_url
        ]
    )


    # def do_get_all_bank_url(url):
    #     full_bank_url = baseurl + url
    #     pageSource = req.get(full_bank_url).text
    #     tree = etree.HTML(pageSource)
    #     last_page_num = tree.xpath('//a[@class="last"]/@href')[0].split("/")[-2]
    #     all_page_bank_url = []
    #     for i in range(1, int(last_page_num) + 1):
    #         page_sub_bank_source = req.get(full_bank_url + str(i)).text
    #         sub_bank_page_tree = etree.HTML(page_sub_bank_source)
    #         all_page_bank_url.append(
    #             sub_bank_page_tree.xpath('//div[@class="col-md-8"]//tr/td[2]/a/@href'))  # 页面银行名称的链接地址)
    #     return all_page_bank_url
    #
    #
    # def get_all_subbank():
    #     all = []
    #     for i in bank_url:
    #         all.append(do_get_all_bank_url(i))
    #     return all
    #
    #
    # def do_get_all_bank_last_link_url(url):
    #     full_bank_url = baseurl + url
    #     pageSource = req.get(full_bank_url).text
    #     tree = etree.HTML(pageSource)
    #     last_page_link = tree.xpath('//div[@class="col-md-8"]/div[@class="well"]//a/@href')
    #     sheng_link = baseurl + last_page_link[0]
    #     pageSource = req.get(sheng_link).text
    #     tree = etree.HTML(pageSource)
    #     city_name = tree.xpath(
    #         '//ul[@class="pagination"]/li[last()-1]/a/@href')  # 有的地方只有一页没有那么多页  因此很可能匹配到的是空页/bank/301/ ['共393条', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '下一页']
    #     print(url, city_name)
    # if __name__ == "__main__":
    # # for i in bank_url:
    # #     do_get_all_bank_last_link_url(i)
    # with open(r"G:\data_analy\bank.txt","a+") as f:
    #     f.write(json.dumps(get_all_subbank()))

#data = tree.xpath('//div[@class="col-md-8"]//tr/td[2]/a/@href')#页面银行名称的链接地址   '/bank/102100000030/'
#data = tree.xpath('//div[@class="col-md-8"]/div[@class="well"]//a/@href')#页面省份链接地址  '/bank/102/guangdong/'
#data = tree.xpath('//div[@class="col-md-4"]/div[@class="well"]//a/@href')#页面右侧银行网点大全链接地址  '/bank/102/'
        #tree.xpath('//div[@class="col-md-8"]/div[@class="well"]/ul[2]//a/@href')  # 获取某银行某省内含城市提取  '/bank/402/nanjing/'
#ree.xpath('//ul[@class="pagination"]/li/a/text()')#有的地方只有一页没有那么多页  因此很可能匹配到的是空页/bank/301/ ['共393条', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '下一页']

# for i in bank_url:
#     full_bank_url = baseurl+i
#     pageSource = req.get(full_bank_url)
#     tree = etree.HTML(pageSource.text)
#     bank_provence_url = tree.xpath('//div[@class="col-md-8"]/div[@class="well"]//a/@href')#页面省份链接地址