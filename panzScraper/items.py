# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PanzscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    #id", "name", "ean", "rate", "votes", "category", "availability", "delivery", "price", "weight", "producer", "description"
    id = scrapy.Field()
    name = scrapy.Field()
    active = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    net = scrapy.Field()
    gross = scrapy.Field()
    weight = scrapy.Field()
    available = scrapy.Field()
    # img = scrapy.Field()
    # # length = scrapy.Field()
    # # width = scrapy.Field()
