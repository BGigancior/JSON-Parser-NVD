from api_fetch import fetch_data_from_api
from convert_to_csv import create_csv_from_data
from json_formatter import filter_json

create_csv_from_data(fetch_data_from_api(),'test')
filter_json("nvdcve-1.1-2003.json", "wynik.json", "attackVector", "NETWORK")