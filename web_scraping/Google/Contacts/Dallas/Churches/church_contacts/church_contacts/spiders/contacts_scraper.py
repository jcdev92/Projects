import scrapy
import os

# Business Title
## '//*[@id="akp_tsuid10"]//h2/span/text()'

# Direction
## PATH 1  -----  '//*[@id="akp_tsuid10"]//div[2]/div/div/span[2]/text()'
## PATH 2  -----  '//*[@id="akp_tsuid10"]//div[3]/div/div[2]/div/div/span[2]/text()'

# Phone Number 
## '//li[@class="next"]/a/@href'

# Website URL 
## //span[@class="text" and @itemprop="text"]/text()

class contactsSpider(scrapy.Spider):
    name = 'churches75230'
    start_urls = [
        'https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALiCzsbMzdH5cKVySWwHwp2VH_OZWv80Pg:1651848443994&q=75230+churches&rflfq=1&num=10&sa=X&ved=2ahUKEwjS_-f9jsv3AhW8lWoFHdJRBv0QjGp6BAgdEAE&biw=819&bih=622&dpr=1.49#rlfi=hd:;si:14773528532225268533,l,Cg43NTIzMCBjaHVyY2hlc1oUIg43NTIzMCBjaHVyY2hlcyoCCAOSARNwcmVzYnl0ZXJpYW5fY2h1cmNomgEjQ2haRFNVaE5NRzluUzBWSlEwRm5TVVJSZUhGVVkwRjNFQUWqARAQASoMIghjaHVyY2hlcygA;mv:[[32.9260996,-96.7680381],[32.8625549,-96.8225437]]'
    ]
    if os.path.exists('contacts.csc'):
        os.remove("contacts.csc")
    
    custom_settings = {
        "FEEDS":{"contacts.css":{"format":"css"}}
    }

    def parse(self, response):
        name = response.xpath('//*[@id="akp_tsuid10"]//h2/span/text()').get()
        direction = response.xpath('//*[@id="akp_tsuid10"]//div[2]/div/div/span[2]/text()').get()
        number = response.xpath('').get()
        website = response.xpath('').get()
        
        web = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').get()
        
        yield {
            'organitation': name,
            'direction': direction,
            'number': number,
            'website': website
        }

        next_page_button_link = response.xpath('').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)       
