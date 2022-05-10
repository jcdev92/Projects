import json
from outscraper import ApiClient

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTE0OTA0MzI1MDM2NTczMTMwODl8NDc3MzA4N2MxNw')

# Search for businesses in specific locations:
result = api_client.google_maps_search('medical centers dallas', limit=200, language='es')

with open('maps_result.json', 'w') as file:
    json.dump(result, file, indent=4)
