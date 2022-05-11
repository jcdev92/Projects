import json
from outscraper import ApiClient

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTE0OTA0MzI1MDM2NTczMTMwODl8NDc3MzA4N2MxNw')

webs = [
] 


webs_2 = [

]

webs_3 = [
   
]

# Search for businesses in specific locations:
result = api_client.emails_and_contacts(webs)

with open('/home/gordo/jmcg_dev/Projects/web_scraping/maps_scraper/json_files/hoas_contacts.json', 'w') as file:
    json.dump(result, file, indent=4)