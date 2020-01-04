# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, TakeFirst, Identity, Join

class GameItemLoader(ItemLoader):
    
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    

class Game(scrapy.Item):
    
    # basic information
    title = scrapy.Field()
    subtitle = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    iap = scrapy.Field()
    age = scrapy.Field()
    desc = scrapy.Field(output_processor = Join()) 
    
    # game popularity and reception
    list_rank = scrapy.Field() #is this game ranked? if so what category and position?
    score = scrapy.Field() #rating
    nrating = scrapy.Field() #number of ratings
    stars = scrapy.Field(output_processor = Identity())
    
    # other details
    editor = scrapy.Field() #game noted by editor?
    seller = scrapy.Field()
    size = scrapy.Field()
    category = scrapy.Field()
    compat = scrapy.Field() #hardware compatibility
    lang = scrapy.Field(input_processor = Compose(lambda v: v[1])) # language in second element of list returned by xpath
    age_copy = scrapy.Field(output_processor = Identity()) # age AND copyright in an unorganized list to be cleaned later
    support = scrapy.Field(output_processor = Identity()) # list of features supported
    
    
    
    

    
