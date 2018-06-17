# -*- coding:euc-kr -*
import scrapy
from testlist.items import ElevenItem

class eleven(scrapy.Spider) :
    handle_httpstatus_list =[404]
    name = "eleven"
    allowed_domains =["11st.co.kr"]
    start_urls = [
            "http://www.11st.co.kr/html/bestSellerMain1.html",
            "http://www.11st.co.kr/html/bestSellerMain2.html",
            "http://www.11st.co.kr/html/bestSellerMain3.html",
            "http://www.11st.co.kr/html/bestSellerMain4.html",
            "http://www.11st.co.kr/html/bestSellerMain5.html",
            "http://www.11st.co.kr/html/bestSellerMain6.html",
            "http://www.11st.co.kr/html/bestSellerMain7.html",
            "http://www.11st.co.kr/html/bestSellerMain8.html",
            "http://www.11st.co.kr/html/bestSellerMain9.html",
            "http://www.11st.co.kr/html/bestSellerMain10.html",
            "http://www.11st.co.kr/html/bestSellerMain11.html",
            "http://www.11st.co.kr/html/bestSellerMain12.html",


    ]

    def parse(self, response):
        # for href in response.xpath('//ul/li/div[3]/div[3]/div[2]/a/@href'):
        # item['href'] = href.xpath('@href').extract()
        # item['title'] = href.xpath('text()').extract()
        for href in response.css('div.pup_title a::attr(href)'):
            yield response.follow(href, self.parse_detail)
            # item = ElevenItem()
            # item['href'] =href.extract()
            # yield item

    def parse_detail(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        item = ElevenItem()
        item['title'] = extract_with_css('h2::text')
        item['price'] = extract_with_css('strong.sale_price::text')
        yield item

        # yield{
        #     'title': extract_with_css('h2::text'),
        #     'price' :extract_with_css('strong.sale_price::text'),
        #
        # }


    # def parse(self, response) :
    #     for name in response.xpath('//div[1]/div/ul/li/a'):
    #
    #             item = ElevenItem()
    #             item['title'] = name.xpath('text()').extract()
    #             yield item

    # def parse(self, response) :
    #     for sel in response.xpath('//ol/li/div/a/div') :
    #         item = ElevenItem()
    #         item['title'] = sel.xpath('p/text()').extract()
    #         item['price'] = sel.xpath('div/span/strong/text()').extract()
    #         yield item
