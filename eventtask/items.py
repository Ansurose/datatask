# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EventtaskItem(scrapy.Item):
    # define the fields for your item here like:
    event_name = scrapy.Field()
    address = scrapy.Field()
    image = scrapy.Field()
    org_name = scrapy.Field()
    org_url = scrapy.Field()
    org_image = scrapy.Field()
    description = scrapy.Field()
    pass
