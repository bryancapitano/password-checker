import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'

response = requests.get(url)
print(response)

