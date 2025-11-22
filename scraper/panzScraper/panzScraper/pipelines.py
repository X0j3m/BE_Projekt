# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#Simple validation on scraped product
#TODO define fields for database, add image_url field for storing path to product images
class PanzscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print("ROZPOCZYNAM PIPELINE")
        price = item['gross']
        gross = price['gross']
        net = price['net']
        adapter['gross'] = gross['base_float']
        adapter['net'] = net['base_float']
        producer = item['producer']
        adapter['producer'] = producer['name']
        weight = item['weight']
        adapter['weight'] = weight['weight_float']
        return item

