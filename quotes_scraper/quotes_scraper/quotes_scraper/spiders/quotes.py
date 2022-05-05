import scrapy

class quotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        print('*'*10)
        print('\n\n')
        print(response.status, response.header)
        print('*'*10)
        print('\n\n')