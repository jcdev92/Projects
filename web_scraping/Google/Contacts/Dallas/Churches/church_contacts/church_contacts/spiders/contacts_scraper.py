import scrapy
import os

# Business Title
## '//h2[@class="qrShPb kno-ecr-pt PZPZlf q8U8x PPT5v hNKfZe"]/span/text()'

# Direction
## PATH 1  -----  '//*[@id="akp_tsuid10"]//div[2]/div/div/span[2]/text()'
## PATH 2  -----  '//*[@id="akp_tsuid10"]//div[3]/div/div[2]/div/div/span[2]/text()'

# Phone Number 
## response.xpath('//a[@data-dtype="d3ph"]//span/text()').get()

# Website URL 
## response.xpath('//a[@class="ab_button CL9Uqc"]/@href').get()

class contactsSpider(scrapy.Spider):
    name = 'churches75230'
    start_urls = [
        'https://www.google.com/search?q=75230%20churches'
    ]
#    if os.path.exists('contacts.csc'):
#        os.remove("contacts.csc")
    
    custom_settings = {
        "FEEDS":{"contacts.css":{"format":"css"}}
    }

    def parse(self, response):
        name = response.xpath('//h2[@class="qrShPb kno-ecr-pt PZPZlf q8U8x PPT5v hNKfZe"]/span/text()').get()
        direction = response.xpath('//span[@class="LrzXr"]/text()').get()
        number = response.xpath('//a[@data-dtype="d3ph"]//span/text()').get()
        website = response.xpath('//a[@class="ab_button CL9Uqc"]/@href').get()
        
        yield {
            'organitation': name,
            'direction': direction,
            'number': number,
            'website': website
        }

        next_page_button_link = response.xpath('//a[@class="fl"]/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)       
