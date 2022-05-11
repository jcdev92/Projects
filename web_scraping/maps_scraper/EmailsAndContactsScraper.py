import json
from outscraper import ApiClient

# import openpyxl
#  
# doc = openpyxl.load_workbook ("webs.xlsx")
# hoja = doc.get_sheet_by_name("webs")
#  
# webs=[]
# for row in hoja.iter_rows():
#     pages = row[1].value
#     webs.append(pages)

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTE0OTA0MzI1MDM2NTczMTMwODl8NDc3MzA4N2MxNw')

short_list = ['https://www.liveatindio.com/lakewood-lodge',
        'https://hoa-community.com/the-warrington-hoa-dallas-tx/',
        'https://www.hillwoodcommunities.com/',
        'https://www.lakeforestdallas.org/home/'
] 

# Search for businesses in specific locations:
result = api_client.emails_and_contacts(short_list)

with open('/home/gordo/jmcg_dev/Projects/web_scraping/maps_scraper/json_files/hoas_contacts.json', 'w') as file:
    json.dump(result, file, indent=4)