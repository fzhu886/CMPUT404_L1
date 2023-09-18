import requests

hmpg = requests.get('http://google.com')
print(hmpg.text)
