# -*- coding: utf-8 -*-
from scrapy.item import Item, Field

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapythonItem(Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
#    pass
