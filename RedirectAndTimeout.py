import requests
from requests.auth import *
from utilities.configurations import *
from utilities.resources import *

url= getConfig()['API']['github']+ApiResources.deleteRepo
se = requests.session()
se.auth = HTTPBasicAuth('vinothiniaut09@gmail.com', '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')
response = se.get(url,allow_redirects =False)
print(response.status_code)
print(response.text)

#Delete repo
response= se.delete(url)
print(response.status_code)

#TimeOut
response = se.get(url,allow_redirects =False, timeout =1)
print(response.status_code)
print(response.text)
