import scrapy
import os
from time import sleep
from ..items import LaptopItem

class LazadaSpider(scrapy.Spider):
    name = 'lazada'
    allowed_domains = ['lazada.vn']
    #  Đọc file  chứa các đường dẫn sản phẩm
    file = open('../data/lazada_link.txt', 'r', encoding='UTF-8')  
    start_urls = file.readlines() 
    file.close()  

    def parse(self, response):
        sleep(5)        # Nghỉ 1 tí tránh bị quét
        # get giá trị dựa vào xpath
        product = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        price = response.xpath('//*[@id="module_product_price_1"]/div/div/div/span[1]/text()').get()
        tag = response.xpath('//*[@id="J_breadcrumb"]/li[3]/span/a/span/text()').get()
        discount = response.xpath('//*[@id="module_product_price_1"]/div/div/div/span[2]/text()').get()
        new_price = response.xpath('//*[@id="module_product_price_1"]/div/div/span/text()').get()
        brand = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link"]/text()').get()
        shop = response.xpath('//*[@id="module_seller_info"]/div/div[1]/div[1]/div[2]/a[1]/text()').get()
        number_reviews = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-review-summary__link"]/text()').get()
        mall = response.xpath('//div[@class="pdp-mod-product-badge-wrapper"]/img[1]').get()
        try:
            if len(mall)>0:
                mall = "Mall"
        except:
            mall = "Non-Mall"

        # Lưu các thông tin vừa get được vào trong class
        item = LaptopItem()
        item["product"] = product
        item['price'] = price
        item['tag'] = tag
        item['discount'] = discount
        item['new_price'] = new_price
        item['brand'] = brand
        item['shop'] = shop
        item['mall'] = mall
        item['number_reviews'] = number_reviews
        yield item
