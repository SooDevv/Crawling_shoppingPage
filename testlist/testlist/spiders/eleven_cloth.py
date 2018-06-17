# -*- coding:euc-kr -*
import scrapy
from testlist.items import ElevenItem

class eleven(scrapy.Spider) :
    name = "cloth"
    allowed_domains =["11st.co.kr"]
    start_urls = [
            "http://www.11st.co.kr/html/bestSellerMain2.html",
    ]

    def parse(self, response):

        for href in response.css('div.pup_title a::attr(href)'):
            yield response.follow(href, self.parse_detail)

        def parse_detail(self, response):
            def extract_with_css(query):
                return response.css(query).extract_first().strip()

            item = ElevenItem()
            item['head'] = extract_with_css('haed')
            yield item
