# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class PanzscraperPipeline:
    def process_item(self, item, spider):
        pass
        # adapter = ItemAdapter(item)
        # field_names = adapter.field_names()
        # for field in field_names:
        #     if field == 'delivery_time':
        #         value = adapter.__getitem__(field)
        #         value = value.split()
        #         adapter[field] = value[0]
        #     elif field == 'price':
        #         value = adapter.__getitem__(field)
        #         value = value.split(",")
        #         adapter[field] = value[0] + "." + "00"
        #     else:
        #         value = adapter.__getitem__(field)
        #         adapter[field] = value.strip()
        # return item
