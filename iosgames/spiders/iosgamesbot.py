# -*- coding: utf-8 -*-
import scrapy
from ..items import GameItemLoader, Game

class Iosgamesbot(scrapy.Spider):
    
    name = 'iosgamesbot'
    allowed_domains = ['apps.apple.com/us/app/simcity-buildit/id913292932']
    start_urls = ['http://apps.apple.com/us/app/simcity-buildit/id913292932/']

    def parse(self, response):
        
        il = GameItemLoader(item=Game(), response=response)

        il.add_xpath('title', '//h1[@class="product-header__title app-header__title"]/text()')
        il.add_xpath('subtitle', '//h2[@class="product-header__subtitle app-header__subtitle"]/text()')
        il.add_xpath('author', '//h2[@class="product-header__identity app-header__identity"]/a/text()')
        il.add_xpath('list_rank', '//li[@class="inline-list__item"]/text()')
        il.add_xpath('price', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]/text()')
        il.add_xpath('iap', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase"]/text()')
    
        
        return il.load_item()
