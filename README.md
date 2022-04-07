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
