# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ElevenItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()

class authorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()
