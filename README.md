## Crawling_shoppingPage

- 개인 맞춤형 추천 쇼핑앱을 개발하기 위한 데이터 수집 작업
- Crawling Site : Coupang, 11번가

### Test Environment

- Language : Python
- OS : Linux(Ubuntu)
- Tool : Atom
- Library : Scrapy

### Installation

[stackoverflow 참고](https://stackoverflow.com/questions/22556965/how-to-install-scrapy-on-ubuntu)

![image](https://user-images.githubusercontent.com/33097467/41509890-190dd11a-7296-11e8-93d7-06c33cc97c09.png)

### Work Flow  

1. 크롤링 대상 확인
> 쇼핑관련 데이터를 모을 수 있는 웹 사이트 선정

2. Scrapy 프로젝트 생성
  - testlist

3. Item 파일 작성
> 수집할 데이터 구조 정의
```
>> tems.py
class ElevenItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
```

4. Spider 파일 작성
> 데이터 수집을 위한 수행 코드를 정의
```
>> eleven_cloth.py
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
```

5. Pipelines 파일 작성(파일저장,DB저장,이메일발송 등)
> 수집된 데이터의 처리 방식 정의
```
>> pipelines.py 중 일부

class JsonPipeline(object):
    def __init__(self):
        self.file = open("eleven.json" , 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
```

6. Settings 파일 작성
> 프로젝트 모듈간 연결 및 기본 설정
> settings.py


7. 프로젝트 실행
> shell 에서 크롤링할 스파이더 실행

```
scrapy crawl eleven_cloth
```

8. 추출 결과(데이터) 확인
> eleven.json
