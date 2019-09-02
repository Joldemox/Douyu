# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json


# 设置翻页循环
class DouyuSpider(scrapy.Spider):
    name = 'douyu2'

    # 每次的初始化都要注意域名范围
    allowed_domains = ['douyu.com']
    base_url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    page = 1
    start_urls = [base_url.format(page)]

    def parse(self, response):
        data_list = json.loads(response.body.decode())['data']['list']

        # 如果没有数据，表示已经抓取完毕
        if not data_list:
            return

        for room in data_list:
            item = DouyuItem()
            item['rid'] = room['rid']
            item['roomName'] = room['roomName']
            item['roomSrc'] = room['roomSrc']
            item['nickname'] = room['nickname']
            item['hn'] = room['hn']

            yield item

        self.page += 1
        url = self.base_url.format(self.page)
        yield scrapy.Request(url, callback=self.parse)
