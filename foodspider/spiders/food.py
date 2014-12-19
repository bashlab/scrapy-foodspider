from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from foodspider.items import FoodItem

class FoodSpider(CrawlSpider):

    name = 'food'
    allowed_domains = ['consumer.org.hk']
    start_urls = ['http://www3.consumer.org.hk/pricewatch/supermarket']
    rules = [Rule(LinkExtractor(allow=['/\?lang=en']), 'parse_food')]

    #@staticmethod
    #def checkHelper(result,tdx):

    def parse_food(self, response):
        hxs = Selector(response)
        results = hxs.xpath('//form[@name=\'itemlist\']/table[2]/tr')
        basket = []
        for result in results:
            food = FoodItem()
            food['category'] = result.xpath('./td[2]/text()').extract()[0].strip()
            food['brand'] = result.xpath('./td[3]/text()').extract()[0].strip()
            food['product'] = result.xpath('./td[4]/a/text()').extract()
            food['price_wellcome'] = result.xpath('./td[5]/text()').extract()[0].strip()
            food['price_pnshop'] = result.xpath('./td[6]/text()').extract()[0].strip()
            food['price_mktplc'] = result.xpath('./td[7]/text()').extract()[0].strip()
            food['price_aeon'] = result.xpath('./td[8]/text()').extract()[0].strip()
            food['price_dch'] = result.xpath('./td[9]/text()').extract()[0].strip()
            food['last_update'] = result.select('./td[10]/text()').extract()[0].strip()
            basket.append(food)
        return basket
