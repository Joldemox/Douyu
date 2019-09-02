# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exporters import CsvItemExporter


# requests请求
# 1、获取图片url
# 2、发送图片请求
# 3、写入本地保存（如果存储云服务器，例如七牛云，则在本地保存存储的url）

# 使用scrapy中的imagesPipline图片下载管道下载图片
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from .settings import IMAGES_STORE
import os


class DouyuImagePipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 1、获取图片url
        image_url = item['roomSrc']

        # 2、发送图片请求
        yield Request(image_url)

        # 3、写入本地保存
        # 在setting中写入IMAGES_STORE 标明当前文件夹下文件名称及路径

    # 图片下载完毕之后，用于更换图片名称
    def item_completed(self, results, item, info):
        # 老图片路径
        old_path = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]

        # 新图片路径
        new_path = IMAGES_STORE + item['nickname'] + '.jpg'

        # OS替换名称rename()
        os.rename(old_path, new_path)

        return item


# CSV文件管道
class DouyuPipeline(object):
    def open_spider(self, spider):
        self.file = open('douyu.csv', 'wb')
        self.writer = CsvItemExporter(self.file)
        self.writer.start_exporting()

    def close_spider(self, spider):
        self.writer.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.writer.export_item(item)
        return item
