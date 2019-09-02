# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    base_url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    page = 1
    start_urls = [base_url.format(page)]

    def parse(self, response):
        data_list = json.loads(response.body.decode())['data']['list']

        for room in data_list:
            item = DouyuItem()
            item['rid'] = room['rid']
            item['roomName'] = room['roomName']
            item['roomSrc'] = room['roomSrc']
            item['nickname'] = room['nickname']
            item['hn'] = room['hn']

            yield item
