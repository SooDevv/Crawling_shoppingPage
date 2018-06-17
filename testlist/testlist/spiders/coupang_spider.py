import scrapy

class coupang(scrapy.Spider) :
    name = "coupang"
    allowed_domains =["www.coupang.com"]
    start_urls = [
            "http://www.coupang.com/np/categories/186764/"
    ]

    def parse(self, response) :
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f :
            f.write(response.body)
