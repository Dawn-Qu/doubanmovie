# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()#电影排名
    title = scrapy.Field()#电影排名
    score = scrapy.Field()#电影评分
    imgurl = scrapy.Field()#电影封面
    pass
