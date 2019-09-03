# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    collection = scrapy.Field()
    family = scrapy.Field()
    category = scrapy.Field()
    quality_level = scrapy.Field()
    price_fn = scrapy.Field()
    price_mw = scrapy.Field()
    price_ft = scrapy.Field()
    price_ww = scrapy.Field()
    price_bs = scrapy.Field()
    pass
