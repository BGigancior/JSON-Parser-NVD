import requests
import json
api_link = 'https://services.nvd.nist.gov/rest/json/cves/1.0/'
response_API = requests.get(api_link)
print(json.loads(response_API.text))