from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from foodspider.items import FoodItem

class FoodSpider(CrawlSpider):
    name = 'food'
    allowed_domains = ['consumer.org.hk']
    start_urls = ['http://www3.consumer.org.hk/pricewatch/supermarket']
    rules = [Rule(LinkExtractor(allow=['/\?lang=en']), 'parse_food')]

    def parse_food(self, response):
        hxs = Selector(response)
        results = hxs.xpath('//form[@name=\'itemlist\']/table[2]/tr')
        basket = []
        for result in results:
            food = FoodItem()
            food['category'] = self.extract_one(result,2)
            food['brand'] = self.extract_one(result,3)
            food['product'] = result.xpath('./td[4]/a/text()').extract()
            food['price_wellcome'] = self.extract_one(result,5)
            food['price_pnshop'] = self.extract_one(result,6)
            food['price_mktplc'] = self.extract_one(result,7)
            food['price_aeon'] = self.extract_one(result,8)
            food['price_dch'] = self.extract_one(result,9)
            food['last_update'] = self.extract_one(result,10)
            basket.append(food)
        return basket


    @staticmethod
    def extract_one(result,idx):
        xp = './td['+str(idx)+']/text()'
        return result.xpath(xp).extract()[0].strip()
