# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GameItemLoader, Game

class Ioscasualcrawler(CrawlSpider):
    
    name = 'ioscasualcrawler'
    allowed_domains = ['apps.apple.com']
    start_urls = ['https://apps.apple.com/us/genre/ios-games-casual/id7003?letter=A']

    rules = (
        # paginate by letter
        Rule(LinkExtractor(allow = 'genre/ios-games-casual/id7003\?letter=(\D)')),
        # paginate to next page
        Rule(LinkExtractor(allow = 'genre/ios-games-casual/id7003\?letter=(\D)&page=(\d+)#page', restrict_xpaths = '//a[@class="paginate-more"]')),
        # go to actuall app description page
        Rule(LinkExtractor(allow = 'app\/(.+)\/id(\d+)', restrict_xpaths = '//div[@id="selectedcontent"]'), callback = 'parse_game'),

    )
        
    def parse_game(self, response):
        
        il = GameItemLoader(item = Game(), response=response)

        # basic information
        il.add_xpath('title', '//h1[@class="product-header__title app-header__title"]/text()')
        il.add_xpath('subtitle', '//h2[@class="product-header__subtitle app-header__subtitle"]/text()')
        il.add_xpath('author', '//h2[@class="product-header__identity app-header__identity"]/a/text()')
        il.add_xpath('price', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--price"]/text()')
        il.add_xpath('iap', '//li[@class="inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase"]/text()')
        il.add_xpath('age', '//span[@class="badge badge--product-title"]/text()')
        il.add_xpath('desc', '//div[@class="section__description"]//p/text()')
        
        # game popularity and reception
        il.add_xpath('list_rank', '//li[@class="inline-list__item"]/text()')
        il.add_xpath('score', '//span[@class="we-customer-ratings__averages__display"]/text()')
        il.add_xpath('nrating', '//div[@class="we-customer-ratings__count small-hide medium-show"]/text()')
        il.add_xpath('stars', '//div[@class="we-star-bar-graph__row"]/div/div/@style')
        
        # other details 
        il.add_xpath('editor', '//div[@class="we-editor-notes lockup ember-view"]/div/h3/text()')
        il.add_xpath('seller', '//dl[@class="information-list information-list--app medium-columns"]/div[1]/dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()')
        il.add_xpath('size', '//dl[@class="information-list information-list--app medium-columns"]/div[2]/dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()')
        il.add_xpath('category', '//dl[@class="information-list information-list--app medium-columns"]/div[3]/dd/a/text()')
        il.add_xpath('compat', '//dl[@class="information-list information-list--app medium-columns"]//p/text()')
        il.add_xpath('lang', '//dl[@class="information-list information-list--app medium-columns"]//p/text()')
        il.add_xpath('age_copy', '//dl[@class="information-list information-list--app medium-columns"]/div//dd/text()')
        il.add_xpath('support', '//div[@class="supports-list__item__copy"]/h3[@dir="ltr"]/text()')
        
        return il.load_item()
