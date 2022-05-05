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
        short = ""
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        for i in quotes:
            short = i
            yield short
        short_tag = ""
        ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        for n in ten_tags:
            short_tag = n
            yield short_tag
        
        yield {
            'title': title,
            'quote' : short,
            'ten_tags': short_tag
        }
        
