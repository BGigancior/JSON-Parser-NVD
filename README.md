# JSON-Parser-NVD

## api-fetch.py

File with function that fetch data from NVD api and return a list of dicts with cves.
Below you can find how to install dependencies needed for this script and usage example.

### Install dependencies

```
pip3 install requests
```

and also if needed:

```
pip3 install json
```

### Example of usage:

```python3
from api_fetch import fetch_data_from_api

print(fetch_data_from_api())
```

## convert_to_csv.py

Script that converts dict to csv file. Function takes two parameters the first one is dict which we want to convert and the second one is the name of the csv file(String!)

### Example of usage:

```python3
from api_fetch import fetch_data_from_api
from convert_to_csv import create_csv_from_data

create_csv_from_data(fetch_data_from_api(),'test')
```
