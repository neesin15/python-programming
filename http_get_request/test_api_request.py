import requests
from requests.exceptions import HTTPError

url = 'https://api.github.com'
try:
    response = requests.get(url)
    print(f'Response code is: {response.status_code}')
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')
    print(f'Response text: \n{response.text}')
