# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import pymysql


class DoubanmoviePipeline:
    def process_item(self, item, spider):
        print('电影排名:{0}'.format(item['rank']))
        print('电影主题:{0}'.format(item['title']))
        print('电影分数:{0}'.format(item['score']))
        print('电影链接:{0}'.format(item['imgurl']))
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item['imgurl']
        yield Request(img_url, meta={'rank': item['rank'], 'name': item['title']})

    def file_path(self, request, response=None, info=None):
        image_rank = request.meta['rank']
        image_name = request.meta['name']
        return '%s-%s.jpg' % (image_rank, image_name)


class MysqlPipeline(object):
    def open_spider(self, spider):
        db_name = spider.settings.get('MYSQL_DB_NAME', 'douban')
        self.db_conn = pymysql.connect('localhost', 'root', '', db_name )
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        self.db_cur.execute('insert into {} (name,score,rank,img_url)values (\'{}\',{},{},\'{}\');' \
                       .format('movie_rank',item['title'], item['score'], item['rank'], item['imgurl']))
        self.db_conn.commit()
