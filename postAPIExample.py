import requests
from payloads import *
from utilities.configurations import *
from utilities.resources import *

url = getConfig()['API']['endpoint']+ApiResources.addBook
header = {"Content-Type": "application/json;charset=UTF-8"}
addBookResponse = requests.post(url,json=bookAPIPayload('nbwrn'),headers= header)
print(addBookResponse.text)
print(addBookResponse.status_code)
response_ID =addBookResponse.json() #Get response as json format
addBookID=response_ID['ID']
print(addBookID)

url = getConfig()['API']['endpoint']+ApiResources.deleteBook
deleteBookResponse = requests.post(url,json={"ID" : addBookID},headers={"Content-Type": "application/json;charset=UTF-8"})
print(deleteBookResponse)
deleteBookResponse.status_code == 200

deleteBookResponse_Msg=deleteBookResponse.json()
print(deleteBookResponse_Msg)
assert deleteBookResponse_Msg["msg"] == "book is successfully deleted"

