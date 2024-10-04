import requests

# Using k-anonymity hash
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'

response = requests.get(url)
print(response)
print('Something')
