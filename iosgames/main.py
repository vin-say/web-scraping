# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 01:17:42 2019

@author: Vincent Sayseng

The 'main' script to run Scrapy web scrapping of the ios app store (games)
"""


from items import App
from scrapy.loader import ItemLoader

il = ItemLoader(item=App())
il = add_xpath('five_star_per', '//body//div//figure//div/div/div/@style')[0] #.get()
il = add_xpath('four_star_per', '//body//div//figure//div/div/div/@style')[1] #.get()
il = add_xpath('three_star_per', '//body//div//figure//div/div/div/@style')[2] #.get()
il = add_xpath('two_star_per', '//body//div//figure//div/div/div/@style')[3] #.get()
il = add_xpath('one_star_per', '//body//div//figure//div/div/div/@style')[4] #.get()


