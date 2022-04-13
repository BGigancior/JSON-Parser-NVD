import csv
from api_fetch import fetch_data_from_api

def create_csv_from_data(data,name):
    data_file = open(f'{name}.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for cve in data:
        if count == 0:
            header = cve.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(cve.values())
    data_file.close()