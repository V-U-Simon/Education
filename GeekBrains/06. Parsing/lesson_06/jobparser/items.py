# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    skills = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    tax_include = scrapy.Field()
    currency = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()
    company_id = scrapy.Field()
    company_link = scrapy.Field()

    print('*' * 100, 'JobparserItem')
