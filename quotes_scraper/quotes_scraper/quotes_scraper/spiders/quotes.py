import scrapy
# Title
## h1/a/text() 

# Citas 
## //span[@class="text" and @itemprop="text"]/text()

# Top Ten Tags
## //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

class quotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        "FEEDS":{"quotes.json":{"format":"json"}}
    }

    def parse(self, response):
        title = response.xpath('//h1/a/text() ').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        yield {
            'title': title,
            'quotes' : quotes,
            'ten_tags': ten_tags
        }

        next_page_button_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)       
