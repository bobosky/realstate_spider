#!/usr/bin/env python
 
__author__ = "Md Tariq Aziz"

from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
#CSV importer
class CSVRealstateItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
    	#kwargs['delimiter'] = settings.get('CSV_DELIMITER', ',')
        #kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['fields_to_export'] = ['links', 'title', 'subur_name', 'unit_mly_jan', 'unit_mly_feb', 'unit_mly_mar', 'unit_mly_apr', 'unit_mly_may', 
        'unit_mly_jun', 'unit_mly_jul', 'unit_mly_aug', 'unit_mly_sep', 'unit_mly_oct', 'unit_mly_nov', 
        'unit_mly_dec', 'unit_mly_p_jan', 'unit_mly_p_feb', 'unit_mly_p_mar', 
        'unit_mly_p_apr', 'unit_mly_p_may', 'unit_mly_p_jun', 'unit_mly_p_jul', 'unit_mly_p_aug', 'unit_mly_p_sep', 
        'unit_mly_p_oct', 'unit_mly_p_nov', 'unit_mly_p_dec', 'unit_mly_nos_jan', 
        'unit_mly_nos_feb', 'unit_mly_nos_mar', 'unit_mly_nos_apr', 'unit_mly_nos_may', 'unit_mly_nos_jun', 
        'unit_mly_nos_jul', 'unit_mly_nos_aug', 'unit_mly_nos_sep', 'unit_mly_nos_oct', 'unit_mly_nos_nov', 'unit_mly_nos_dec',]

        #kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')
        super(CSVRealstateItemExporter, self).__init__(*args, **kwargs)