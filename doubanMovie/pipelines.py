# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class DoubanmoviePipeline:
    def process_item(self, item, spider):
        print('电影排名:{0}'.format(item['rank'][0]))
        print('电影主题:{0}'.format(item['title'][0]))
        print('电影分数:{0}'.format(item['score'][0]))
        print('电影链接:{0}'.format(item['imgurl'][0]))
        return item
