import scrapy
import re
from ..items import LaptopItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from scrapy.utils.project import get_project_settings


class TikiSpider(scrapy.Spider):
    name = 'tiki'
    allowed_domains = ['tiki.vn']
    start_urls = ['https://tiki.vn/may-tinh-xach-tay-laptop-dell-latitude-3420-l3420i3ssd-intel-core-i3-1115g4-14-inch-hd-ram-8gb-256gb-ssd-nvme-intel-uhd-graphics-fedora-os-hang-chinh-hang-p113577973.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.35831_Y.271589_Z.1223547_CN.Laptop&itm_medium=CPC&itm_source=tiki-ads&spid=113577975',
    'https://tiki.vn/apple-macbook-air-2020-m1-13-inchs-hang-chinh-hang-p124742926.html?spid=88231360']

    def parse(self, response):
        
        product = response.xpath('///*[@class="title"]/text()').get()
        price = response.xpath('//*[@class="product-price__list-price"]/text()').get()
        tag = 0 #response.xpath('//*[@id="__next"]/div[1]/main/div[1]/div/div/a[4]/span/text()').get()
        discount = 0 #response.xpath('//*[@class="product-price__discount-rate"]/text()').get()
        new_price = 0 #response.xpath('//*[@class="product-price__current-price"]/text()').get()
        brand = 0 #response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[1]/span/h6/a/text()').get()
        shop = 0 #response.xpath('//*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div[1]/a/div/span/span/text()').get()
        number_reviews = 0 #response.xpath('//a[@class="pdp_main_view_review"]/text()').get()
        mall = 0 #response.xpath('//div[@class="WebpImg__StyledImg-sc-h3ozu8-0 fWjUGo badge-img"]/img[1]').get()
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
