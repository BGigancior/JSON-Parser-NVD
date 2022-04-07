import requests
import json

def fetch_data_from_api():
    api_link = 'https://services.nvd.nist.gov/rest/json/cves/1.0/'
    response_API = requests.get(api_link)
    data = json.loads(response_API.text)["result"]["CVE_Items"]
    return data