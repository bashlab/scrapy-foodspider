import scrapy

class FoodItem(scrapy.Item):
    category = scrapy.Field()
    brand = scrapy.Field()
    product = scrapy.Field()
    price_wellcome = scrapy.Field()
    price_pnshop = scrapy.Field()
    price_mktplc = scrapy.Field()
    price_aeon = scrapy.Field()
    price_dch = scrapy.Field()
    last_update = scrapy.Field()
