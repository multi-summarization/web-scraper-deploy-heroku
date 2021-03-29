import scrapy 
import re
import unidecode
from newspaper import fulltext
import requests
from scrapy.http import Request
from ..items import Article

# running: scrapy crawl ndtv -o ndtv_articles.json

class ndtvSpider(scrapy.Spider):
    name = 'ndtv'	

    # def start_requests(self):
        
    start_urls = [
        'https://www.ndtv.com/top-stories/page-1'
    ]

                
    def parse(self, response):

        for article in response.xpath("//h2[@class='newsHdng']"):

            item = Article()

            item['source'] = "NDTV"

            ##### HEADLINE
            item['headline']=article.xpath("normalize-space(.//a/text())").extract_first()

            ##### LINK
            link = article.xpath(".//a/@href").extract_first()
            item['link']= link

            ##### CONTENT
            item['content'] = fulltext(requests.get(link).text)


            yield item
    
        next_page = response.xpath("//a[contains(@class,'next')]/@href").extract_first()
        
        if next_page is not None and next_page[:-1] != '0':
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

# running: scrapy crawl hindustan -o hindustan_articles.json

class hindustanSpider(scrapy.Spider):
    name = 'hindustan'	
    # art = Article()
    # def start_requests(self):
        
    start_urls = [
        'https://www.hindustantimes.com/latest-news'
    ]

    def parse_article(self, response):
        ##### CONTENT
        paras=response.xpath("//div[@class='detail']/p").extract()
        item = response.meta['article_object']
        item['content'] = "".join(paras)
        return item

                
    def parse(self, response):
        for article in response.xpath("//div[@class='storyShortDetail']/descendant::a[not(parent::div)]"):
            

            ##### HEADLINE
            headline=article.xpath("normalize-space(./text())").extract_first()

            ##### LINK
            link='https://www.hindustantimes.com' + article.xpath("./@href").extract_first()

            item = Article()

            req = Request(link, callback=self.parse_article)
            req.meta['article_object'] = item
            item['source'] = "HindustanTimes"
            item['headline'] = headline
            item['link'] = link
            
            #the request is executed on the below line with the item being passed as meta attribute. pasrse_article callback is executed.
            yield req


        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        
        if next_page is not None and next_page[:-1] != '0':
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

# running: scrapy crawl ie -o ie_articles.json

class ieSpider(scrapy.Spider):
    name = 'ie'	
    # art = Article()
    # def start_requests(self):
        
    start_urls = [
        'https://indianexpress.com/latest-news/'
    ]
          
    def parse(self, response):

        for article in response.xpath("//div[@class='title']/a"):

            item = Article()

            item['source'] = "ie"

            ##### HEADLINE
            item['headline']=article.xpath("normalize-space(./text())").extract_first()

            ##### LINK
            link = article.xpath("./@href").extract_first()
            item['link']= link

            ##### CONTENT
            item['content'] = fulltext(requests.get(link).text)


            yield item
    
        next_page = response.xpath("//ul[@class='page-numbers']/li[position()=11]/a/@href").extract_first()
        
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
