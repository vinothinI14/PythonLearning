import requests
from utilities.configurations import *


url="https://petstore.swagger.io/v2/pet/9843217/uploadImage"
filepath = "C:\\Users\\ADMIN\\Downloads\\Premises_Photo.png"
file = {'file':open(filepath, 'rb')}
response = requests.post(url,files =file)
print(response.status_code)
print(response.text)