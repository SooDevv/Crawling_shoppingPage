from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
import html2text


class WikiSpider(BaseSpider):
    name = "wiki_spider"
    allowed_domains = ["www.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_(programming_language)"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sample = hxs.select("//div[@id='mw-content-text']/p[1]").extract()[0]

        converter = html2text.HTML2Text()
        converter.ignore_links = True
        print(converter.handle(sample)) #Python 3 print syntax
