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
        'https://www.google.com/search?q=75230%20churches&oq=75&aqs=chrome.0.69i59j69i57j69i59j0i512j46i512j69i65j69i60l2.1392j0j7&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALiCzsYr1_AnbPjV1l7413vSWnbN8lV4oQ:1651860160914&rflfq=1&num=10&rldimm=5676161483414474647&lqi=Cg43NTIzMCBjaHVyY2hlc1oUIg43NTIzMCBjaHVyY2hlcyoCCAOSARBtZXRob2Rpc3RfY2h1cmNoqgEQEAEqDCIIY2h1cmNoZXMoAA&ved=2ahUKEwjxhvDQusv3AhWQlmoFHRiQBG0QvS56BAgEEAE&sa=X&rlst=f#rlfi=hd:;si:5676161483414474647,l,Cg43NTIzMCBjaHVyY2hlc1oUIg43NTIzMCBjaHVyY2hlcyoCCAOSARBtZXRob2Rpc3RfY2h1cmNoqgEQEAEqDCIIY2h1cmNoZXMoAA;mv:[[32.9260996,-96.7680381],[32.8625549,-96.8225437]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2'
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
