# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GameItemLoader, Game

class Iosgamescrawler(CrawlSpider):
    
    name = 'iosgamescrawler'
    allowed_domains = ['apps.apple.com']
    start_urls = ['https://apps.apple.com/us/genre/ios-games/id6014?letter=A&page=1#page']

    rules = (
        # paginate by letter
        Rule(LinkExtractor(allow = ('genre/ios-games/id6014\?letter=(\D)&page=(\d+)#page'))),
        Rule(LinkExtractor(allow = 'app\/(.+)\/id(\d+)', restrict_xpaths = '//div[@id="selectedcontent"]'), callback = 'parse_game'),
#        Rule(LinkExtractor(allow = 'app\/(.+)\/id(\d+)'), callback = 'parse_game'),

    )
        
    def parse_game(self, response):
        
        il = GameItemLoader(item = Game(), response=response)

        il.add_xpath('title', '//h1[@class="product-header__title app-header__title"]/text()')
        il.add_xpath('subtitle', '//h2[@class="product-header__subtitle app-header__subtitle"]/text()')
        il.add_xpath('author', '//h2[@class="product-header__identity app-header__identity"]/a/text()')
        il.add_xpath('list_rank', '//li[@class="inline-list__item"]/text()')
        il.add_xpath('price', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]/text()')
        il.add_xpath('iap', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase"]/text()')
    
        
        return il.load_item()
