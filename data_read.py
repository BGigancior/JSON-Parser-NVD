import json

def read_data(start, end):
    data = []
    for year in range(start,end):
        with open('json/nvdcve-1.1-'+str(year)+'.json', 'r', encoding='utf-8') as jsondata:
            temp_data = json.load(jsondata)
            data.extend(temp_data["CVE_Items"])
    return data