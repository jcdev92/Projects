import scrapy
import os

# //div[2]/div/a[1]/div/div/div[1]
# //div[2]/div/a[1]/div/div/div[3]

class mapsSpider(scrapy.Spider):
    name = 'maps'
    allowed_domains = ["https://www.google.com/?hl=es"]
    start_urls = ['https://www.google.com/search?tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ALiCzsY6NwHEcmizK569Vy1KLWEQdeF3fA:1652042344804&q=75230+churches&rflfq=1&num=10&sa=X&ved=2ahUKEwjVu_ao4dD3AhUhRjABHTdiAmQQjGp6BAgeEAE&biw=819&bih=622&dpr=1.49#rlfi=hd:;si:;mv:[[32.9260996,-96.7680381],[32.8625549,-96.8225437]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2']

#    if os.path.exists('contacts.csc'):
#        os.remove("contacts.csc")

    def parse(self, response):
        
        name = response.xpath('//a[1]/div/div/div[1]/span/text()').getall()
        direction = response.xpath('//a[1]/div/div/div[3]/text()').getall()
#        zone = response.xpath('//div[@class="locality"]/text()').getall()
#        number = response.xpath('//div[@class="phones phone primary"]/text()').getall()
        website = response.xpath('//div[1]/div/a[2]/@href').getall() and response.xpath('//div[2]/div/a[2]/@href').getall() and response.xpath('//div[3]/div/a[2]/@href').getall()       
        for i in range(len(name)):
            yield {
            'organitation': name[i],
            'direction': direction[i],
#            'zone': zone[i],
#            'number': number[i],
            'website': website[i],
        }

        next_page_button_link = response.xpath('//td[3]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)     
