import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3MDYzNDg3MiwianRpIjoiNzI0OWU5YWM3NWMyNGE3M2IzZWNkMzYyMjI3NzAxNjIiLCJ1c2VyX2lkIjoxfQ.aEYTldqboHPrLG6ZuLcyEbr8hm653x3OtAYzy04FjWs'
requ = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)
print(requ.text)