import json
from outscraper import ApiClient

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTE0OTA0MzI1MDM2NTczMTMwODl8NDc3MzA4N2MxNw')

# Search for businesses in specific locations:
# result = api_client.google_maps_search('dallas restaurants', limit=200, language='es')

result = api_client.google_maps_search([
    '75219 restaurants',
    '75225 restaurants',
    '75226 restaurants',
    '75230 restaurants'
], language='es')

with open('maps_result.json', 'w') as file:
    json.dump(result, file, indent=4)
