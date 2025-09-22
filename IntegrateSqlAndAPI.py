import requests
from utilities.configurations import *
from utilities.resources import *
from payloads import *


url = getConfig()['API']['endpoint']+ApiResources.addBook
header = {"Content-Type": "application/json;charset=UTF-8"}
query = 'select * from Books'
response = requests.post(url,json=getPayloadFromDB(query),headers= header)
print(response.text)
print(response.status_code)
jsonResponse = response.json()
bookId= jsonResponse['ID']
print(bookId)