# -*- coding: utf-8 -*-
import scrapy
from ..items import GameItemLoader, Game

class Iosgamesbot(scrapy.Spider):
    name = 'iosgamesbot'
    allowed_domains = ['apps.apple.com/us/app/simcity-buildit/id913292932']
    start_urls = ['http://apps.apple.com/us/app/simcity-buildit/id913292932/']

    def parse(self, response):
        il = GameItemLoader(item=Game(), response=response)
        il.add_xpath('title', '//body//header/h1/text()')
        il.add_xpath('subtitle', '//body//header/h2/text()')
            
        return il.load_item()
