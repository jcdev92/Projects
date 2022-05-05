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

    def parse(self, response):
        print('*'*10)
        print('\n\n\n')
        ## print(response.status, response.headers)
        title = response.xpath('//h1/a/text() ').get()
        print(f'Titulo: {title}')
        print('\n\n')

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: ')
        for quote in quotes:
            print(f'- {quote}')
        print('\n\n')

        ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('ten tags: ')
        for tag in ten_tags:
            print(f'- {tag}')
        print('\n\n')
        
        print('\n\n\n')
        print('*'*10)
        