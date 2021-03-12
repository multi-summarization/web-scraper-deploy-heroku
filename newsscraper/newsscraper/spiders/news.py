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
            

            ##### HEADLINE
            headline=article.xpath("normalize-space(.//a/text())").extract_first()

            ##### LINK
            link=article.xpath(".//a/@href").extract_first()

            ##### CONTENT
            content = fulltext(requests.get(link).text)


            yield {
                'headline' : headline,
                'link' : link,
                'content': content,

            }
    
        next_page = response.xpath("//a[contains(@class,'next')]/@href").extract_first()
        
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

# running: scrapy crawl hindu -o hindu_articles.json

class hinduSpider(scrapy.Spider):
    name = 'hindu'	
    # art = Article()
    # def start_requests(self):
        
    start_urls = [
        'https://www.hindustantimes.com/latest-news'
    ]

    def parse_article(self, response):
        paras=response.xpath("//div[@class='detail']/p").extract()
        art = response.meta['article_object']
        art['content'] = "".join(paras)
        return art

                
    def parse(self, response):
        for article in response.xpath("//div[@class='storyShortDetail']/descendant::a[not(parent::div)]"):
            

            ##### HEADLINE
            headline=article.xpath("normalize-space(./text())").extract_first()

            ##### LINK
            link='https://www.hindustantimes.com' + article.xpath("./@href").extract_first()

            ##### CONTENT
            art = Article()

            req = Request(link, callback=self.parse_article)
            req.meta['article_object'] = art

            art['headline'] = headline
            art['link'] = link

            yield req

            # yield {
            #     # 'headline': headline,
            #     # 'link': link,
            #     'content': Request(link, callback=self.parse_article),
            # }
    
        # next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        
        # if next_page is not None:
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page_link, callback=self.parse)
