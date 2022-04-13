from api_fetch import fetch_data_from_api
from convert_to_csv import create_csv_from_data

create_csv_from_data(fetch_data_from_api(),'test')