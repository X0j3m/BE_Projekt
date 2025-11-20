# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request 


class PanzscraperPipeline(ImagesPipeline):

    # def get_media_requestes(self, item, info):
    #     description = item['description'].split(" ")
    #     images_urls = [i for i in description if "src" in i]
    #     images_urls = [i.split("=") for i in images_urls]
    #     images_urls = [i[1] for i in images_urls]
    #     print(images_urls)
    #     for url in images_urls:
    #         yield Request(url)
    
    # def item_completed(self, results, item, info):
    #     print(x["path"] for x in results)
    #     return item

    def process_item(self, item, spider):
        return item
    #     print("PIPELINE ZACZYNA PRACE")
    #     description = item['description'].split(" ")
    #     images_urls = [i for i in description if "src" in i]
    #     images_urls = [i.split("=") for i in images_urls]
    #     images_urls = [i[1] for i in images_urls]
    #     print(images_urls)       
    #     return item 
        
    