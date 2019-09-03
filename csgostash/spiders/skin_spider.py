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
        collection_name = \
        Selector(response).xpath('//div[@class="inline-middle collapsed-top-margin"]/h1/text()').extract()[0]
        skins = Selector(response).xpath('//div[@class="col-lg-4 col-md-6 col-widen text-center"]')
        for skin in skins:
            link = skin.xpath('div/div[@class="price"]/p/a/@href').extract_first()
            if link is not None:
                yield response.follow(link, callback=self.parse_skin, meta={'collection': {'name': collection_name}})

    def parse_skin(self, response):
        meta = response.meta['collection']
        skin = SkinItem()
        skin['collection'] = meta['name']
        skin['category'] = 'normal'

        general_info = Selector(response).xpath('//div[@class="well result-box nomargin"]')
        skin['name'] = general_info.xpath('h2/a[0]/text()').extract_first()
        skin['family'] = general_info.xpath('h2/a[0]/text()').extract_first()

        prices = Selector(response).xpath('//div[@id="prices"]/div[@class="btn-group-sm btn-group-justified"]')
        for price in prices:
            info = price.xpath('a/span')
            if len(info) == 2:
                type = price.xpath('a/span[@class="pull-left"]/text()').extract_first()
                price = price.xpath('a/span[@class="pull-right"]/text()').extract_first()[:-1].replace('.','')
                if type == 'Factory New':
                    skin['price_fn'] = int(price) if price.isdigit() else -1
                elif type == 'Minimal Wear':
                    skin['price_mw'] = int(price) if price.isdigit() else -1
                elif type == 'Field-Tested':
                    skin['price_ft'] = int(price) if price.isdigit() else -1
                elif type == 'Well-Worn':
                    skin['price_ww'] = int(price) if price.isdigit() else -1
                elif type == 'Battle-Scarred':
                    skin['price_bs'] = int(price) if price.isdigit() else -1


        print(skin)
# yield skin
