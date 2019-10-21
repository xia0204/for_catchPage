# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

#丢弃数据项




class MaitianPipeline(object):
    def __init__(self):
        self.host = settings["MONGODB_HOST"]
        self.port = settings["MONGODB_PORT"]
        self.dbname = settings["MONGODB_DBNAME"]
        self.docname = settings["MONGODB_DOCNAME"]
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host=self.host,port=self.port)
        db = self.client[self.dbname]
        self.post = db[self.docname]#链接mongodb
    def close_spider(self,spider):
        self.client.close()
    def process_item(self, item, spider):#重点实现函数 实现内容要将提取出来的数据内容插到数据库中 持久化模块
        paper = dict(item)
        self.post.insert(paper)
        return item

class testPipeline(): #通过集合去重
    def __init__(self):
        self.ids_seen = set()
    def process_item(self,item,spider):
        if item["id"] in self.ids_seen:
            raise DropItem("id %s has been in set "%item)
        else:
            self.ids_seen.add(item["id"])
            return item


"""
class testPipeline(object):
    vot_fact = 1.15

    def process_item(self, item, spider):
        if item["price"]:
            if item["peice_exculedes_vot"]:
                item["price"] = item["price"] * self.vot_fact
            return item
        else:
            raise DropItem("missing price in %s"%item)
        return item

"""