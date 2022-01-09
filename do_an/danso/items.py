# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LaptopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Tên sản phẩm
    product = scrapy.Field()
    # Danh mục
    tag = scrapy.Field()
    # Giá gốc
    price = scrapy.Field()
    # Discount
    discount = scrapy.Field()
    # Giá sau khi giảm
    new_price = scrapy.Field()
    # Thương hiệu
    brand = scrapy.Field()
    # Cửa hàng phân phối:
    shop = scrapy.Field()
    # Mall or None
    mall = scrapy.Field()
    # Chất lượng trung bình
    number_reviews = scrapy.Field()
