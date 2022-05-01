import requests
import lxml.html as html
import os
import datetime

XPATH_LINK_TO_ARTICLE = '//div[@class="V_Title"]/a/@href'
XPATH_TITLE = '//h2[@data-h="45"]/span/text()'
XPATH_SUMMARIES = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()'

HOME_URL = 'https://www.larepublica.co/'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)
        

def run():
    parse_home()

if __name__ == '__main__':
    run()