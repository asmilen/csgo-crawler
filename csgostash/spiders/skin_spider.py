# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector

from csgostash.items import SkinItem


class SkinSpider(CrawlSpider):
    name = "skin"
    allowed_domains = ["csgostash.com"]
    start_urls = [
        "https://csgostash.com/collection/The+Dust+2+Collection",
    ]

    def parse(self, response):
        collection_name = Selector(response).xpath('//div[@class="inline-middle collapsed-top-margin"]/h1/text()').extract()[0]
        skins = Selector(response).xpath('//div[@class="col-lg-4 col-md-6 col-widen text-center"]')
        for skin in skins:
            link = skin.xpath('div/div[@class="price"]/p/a/@href').extract_first()
            if link is not None:
                yield response.follow(link, callback=self.parse_skin, meta={'collection': {'name': collection_name}})

    def parse_skin(self, response):
        meta = response.meta['collection']
        skin = SkinItem()
        skin['collection'] = meta['name']
        prices = Selector(response).xpath('//div[@id="prices"]/div[@class="btn-group-sm btn-group-justified"]')
        for price in prices:
            type = price.xpath('a/span[@class="pull-left"]/text()').extract_first()
            if type == 'Factory New':

            elif type == 'Minimal Wear':

            elif type == 'Field-Tested':

            elif type == 'Well-Worn':

            elif type == 'Battle-Scarred':

            else:
        # Do the default
        #yield skin

