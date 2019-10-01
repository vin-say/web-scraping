# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

class GameItemLoader(ItemLoader):
    
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    

class Game(scrapy.Item):
    
    title = scrapy.Field()
    subtitle = scrapy.Field()


    
