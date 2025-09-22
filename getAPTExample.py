import requests
import json
from utilities.configurations import *
from utilities.resources import *

# url = getConfig()['API']['endpoint']+ApiResources.getBook
response = requests.get('http://216.10.245.166/Library/GetBook.php?',params={'AuthorName':'RahulShetty'},)
print(response.text)
list_response=json.loads(response.text)
print(list_response)
print(list_response[0]['isbn'])
#json will return response
responseValue = response.json()
print(responseValue[0]['isbn'])

#Validating status code
print(response.status_code)
assert response.status_code == 200, 'Status code valid'

#Validating headers
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

#Validating cookies
print(response.cookies)

#Retrive book details with ISBN 'RGHCC

for actualBook in response.json():
    if actualBook['isbn'] == 'RGHCC':
        print(actualBook)
        break
expectedBook ={"book_name":"Pythonselenium 18 hrs by Rahulshetty",
               "isbn":"RGHCC",
               "aisle":"11097"
               }
assert actualBook == expectedBook




