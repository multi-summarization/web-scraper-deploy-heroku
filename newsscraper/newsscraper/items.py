# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #source = Field()
    headline = Field()
<<<<<<< HEAD
    #tagline = Field()
    body = Field()
    url = Field()
=======
    link = Field()
    content = Field()
>>>>>>> 04a0dbcacf87a9b4377a3dca3702030f06a73b5d
    #genre = Field()
