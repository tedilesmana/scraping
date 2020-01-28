# -*- coding: utf-8 -*-
import scrapy


class BabastudioSpider(scrapy.Spider):
    name = 'babastudio'
    start_urls = ['https://academy.babastudio.com/course-package-frontend']

    def parse(self, response):
        all_kursus = response.css('div.course__box')
        for kursus in all_kursus:
        	title = kursus.css('p.title::text').extract()
        	price = kursus.css('strong::text').extract()
        	image = kursus.css('img.img-responsive').attrib['src']
        	yield{
        		'title':title,
        		'price':price,
        		'image':image
        	}

