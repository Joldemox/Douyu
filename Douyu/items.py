# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    rid = scrapy.Field()
    roomName = scrapy.Field()
    roomSrc = scrapy.Field()
    nickname = scrapy.Field()
    hn = scrapy.Field()