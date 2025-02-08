import scrapy

class ShoescraperItem(scrapy.Item):
    name = scrapy.Field()
    pass

class ShoeItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    colour = scrapy.Field()
    availableColours = scrapy.Field()
    reviews_count = scrapy.Field()
    reviews_score = scrapy.Field()