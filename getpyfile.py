import requests

hmpg = requests.get('http://github.com/fzhu886/CMPUT404_L1/blob/main/getgooglehmpg.py')
print(hmpg.text)
