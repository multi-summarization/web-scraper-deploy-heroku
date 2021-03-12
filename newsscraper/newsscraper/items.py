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
    link = Field()
    content = Field()
    #genre = Field()
