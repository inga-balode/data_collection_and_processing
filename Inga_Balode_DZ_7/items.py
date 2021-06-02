# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def change_url(value):
    try:
        result = value.replace('w_82', 'w_1200').replace('h_82', 'h_1200')
        return result
    except Exception:
        return value

def change_price(price):
    price = price.replace(' ', '')
    result = int(price)
    return result

def change_specs(value):
    result = value.replace('\n', '').strip()
    return result

class LermerItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(change_url))
    link = scrapy.Field(output_processor=TakeFirst())
    specs_all = scrapy.Field(input_processor=MapCompose(change_specs))
    specs = scrapy.Field(input_processor=MapCompose(change_specs))
    price = scrapy.Field(input_processor=MapCompose(change_price), output_processor=TakeFirst())

