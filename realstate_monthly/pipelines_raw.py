# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
__author__ = 'Tariq'

from scrapy import signals, Field
from scrapy.conf import settings
from realstate_monthly.exporters import CSVRealstateItemExporter
from unidecode import unidecode
import time, os

class RealstateMonthlyPipeline(object):
    def process_item(self, item, spider):
        return item
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        export_dir = settings.get('EXPORT_DIR', '.')
        t = time.strftime('%Y-%m-%d %H-%M-%S GMT+6', time.gmtime(time.time() + 6*3600))
        path = os.path.join(export_dir, '%s.csv' % t)
        self.file = open(path, 'w+b')
        self.exporter = CSVRealstateItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

