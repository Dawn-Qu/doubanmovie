import scrapy
from doubanMovie.items import DoubanmovieItem
#导入DoubanmovieItem类
class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_items = response.xpath('//div[@class="item"]')
        #获取所有电影标签
        for item in movie_items:
            #print(type(item))
            movie = DoubanmovieItem()
            movie['rank'] = item.xpath('div[@class="pic"]/em/text()').extract()
            movie['title'] = item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['score'] = item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie['imgurl'] = item.xpath('div[@class="pic"]/a/img/@src').extract()
            yield movie
        # 获取下一页标签
        new_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
        if new_url:
            new_url = 'http://movie.douban.com/top250' + new_url
            yield scrapy.Request(new_url,callback=self.parse)