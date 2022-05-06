import scrapy
# Title
## h1/a/text() 

# Citas 
## //span[@class="text" and @itemprop="text"]/text()

# Top Ten Tags
## //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

class quotesSpider(scrapy.Spider):
    name = 'quotes_2'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.xpath('//h1/a/text() ').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        
        yield {
            'title': title,
            'quote' : quotes[0],
            'ten_tags': ten_tags[0]
        }

        yield {
            'title': title,
            'quote' : quotes[1],
            'ten_tags': ten_tags[1]
        }



        
