# -*- coding: utf-8 -*-
__author__ = "Tariq"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
from scrapy import signals
from scrapy.exporters import CsvItemExporter, XmlItemExporter
from scrapy import signals, Field
from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
from realstate_monthly.exporters import CSVRealstateItemExporter
from unidecode import unidecode
import json
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import logging
from urlparse import urlparse
import re
import time
reload(sys)
sys.setdefaultencoding('utf8')

class RealstateMonthlyPipeline(object):
    def process_item(self, item, spider):
        return item
    EXPORT_PATH = os.getenv("HOME")

    def __init__(self):
        self.files = {}
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
# @spider_opened_working
    def spider_opened(self, spider):
        export_dir = settings.get('EXPORT_PATH', '.')
        t = time.strftime('%Y-%m-%d %H-%M-%S GMT+6', time.gmtime(time.time() + 6*3600))
        path = os.path.join(export_dir, '%s.csv' % t)
        self.files = open(path, 'w+b')
        self.exporter = CSVRealstateItemExporter(self.files)
        self.exporter.start_exporting()
# End}}}
    # def spider_opened(self, spider):
    #     # self.file = open('%s-%s.csv' % (spider.name, time.strftime("%Y-%m-%d-%H")), 'w+')
    #     path = RealstateMonthlyPipeline.EXPORT_PATH + "/" + spider.name + '_export.csv'
    #     export_file = open(path, 'ab' if os.path.isfile(path) else 'wb')
    #     self.files[spider.name] = export_file
    #     # self.exporter = CsvRealstateItemExporter(self.file)
    #     self.exporter = CSVRealstateItemExporter(self.files)
#         self.exporter.fields_to_export = ['links', 'title', 'subur_name', 'unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may', 
# 'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov', 
# 'unit_mly_dec', 'unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 
# 'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 
# 'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec', 'unit_mly_nos_jan', 
# 'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun', 
# 'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec',
# ]
        # self.exporter.start_exporting()

    # def spider_opened(self, spider):
    #     if spider.name in 'realestate':
    #         self.file = open('current_listing.csv', 'w+b')
    #     else:
    #         self.file = open('past_listing.csv', 'w+b')
    #     self.exporter = CsvItemExporter(self.file)
    #     self.exporter.start_exporting()


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.files.close()

