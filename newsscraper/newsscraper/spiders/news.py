import scrapy 
import re
import unidecode
from newspaper import fulltext
import requests

# running: scrapy crawl ndtv -o ndtv_articles.json

class ndtvSpider(scrapy.Spider):
    name = 'ndtv'	

    # def start_requests(self):
        
    start_urls = [
        'https://www.ndtv.com/top-stories/page-1'
    ]

                
    def parse(self, response):
        items = []

        for article in response.xpath("//h2[@class='newsHdng']"):

            item = NewsscraperItem()

            item['source'] = "NDTV"

            ##### HEADLINE
            item['headline']=article.xpath("normalize-space(.//a/text())").extract_first()

            ##### LINK
            link = article.xpath(".//a/@href").extract_first()
            item['url']= link

            ##### ARTICLE
            item['body'] = fulltext(requests.get(link).text)


            yield {
                'headline' : item['headline'],
                'link' : item['url'],
                'article': item['body'],

            }
            items.append(item)
    
        next_page = response.xpath("//a[contains(@class,'next')]/@href").extract_first()
        
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

        return items
