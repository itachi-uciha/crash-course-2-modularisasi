import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Succes, Response = {response}')
        print(f'content {response.text}')
    else:
        print(f'Oops, ada kesalahan requests {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('program ended')

