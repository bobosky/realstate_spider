# -*- coding: utf-8 -*-
__author__ = 'Tariq'

BOT_NAME = 'realstate_monthly'
SPIDER_MODULES = ['realstate_monthly.spiders']
NEWSPIDER_MODULE = 'realstate_monthly.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0'

FEED_EXPORTERS = {
   'csv': 'realstate_monthly.exporters.CSVRealstateItemExporter',
}

FEED_URI = 'file:///home/.virtualenvs/scrapydevenv/spiders/realstate_monthly/realstate_monthly/scrapyd_export.csv'
FEED_FORMAT = 'csv'
FEED_EXPORTERS = {'my_csv': 'realstate_monthly.exporter.CsvItemExporter'}
FEED_FORMAT = 'csv'
# CSV_DELIMITER = '\t'
#CSV_JOIN_MULTIVALUED = '|'

EXPORT_FIELDS = ['unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may',
'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov',
'unit_mly_dec', 'unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar',
'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep',
'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec', 'unit_mly_nos_jan',
'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun',
'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec',
]

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

ITEM_PIPELINES = {
   'realstate_monthly.pipelines.RealstateMonthlyPipeline': 300,
}

DOWNLOAD_DELAY=3
