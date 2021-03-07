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
        for article in response.xpath("//h2[@class='newsHdng']"):
            

            ##### HEADLINE
            headline=article.xpath("normalize-space(.//a/text())").extract_first()

            ##### LINK
            link=article.xpath(".//a/@href").extract_first()

            ##### ARTICLE
            article = fulltext(requests.get(link).text)


            yield {
                'headline' : headline,
                'link' : link,
                'article': article,

            }
    
        next_page = response.xpath("//a[contains(@class,'next')]/@href").extract_first()
        
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
