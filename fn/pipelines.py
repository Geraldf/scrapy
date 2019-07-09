# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class FnPipeline(object):

    def __init__(self):
        self.df = pd.DataFrame(columns=['Date','Time','Text'])
        

    def process_item(self, item, spider):
        self.df.append(item,ignore_index=True)
        return item
