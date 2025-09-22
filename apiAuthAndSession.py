import requests
from utilities.configurations import *
from requests.auth import HTTPBasicAuth

#Adding auth for api validation

url= "https://api.github.com/user"
git_response = requests.get(url, auth=HTTPBasicAuth('vinothiniaut09@gmail.com', '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'))
# git_response=requests.get(url,auth=('vinothiniaut09@gmail.com', getPassword())) # to avoid ssl certificate error use verify =False
print(git_response)
assert git_response.status_code == 200


#Create and manage session
se = requests.session()
se.auth = HTTPBasicAuth('vinothiniaut09@gmail.com', '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')
url = "https://api.github.com/user/repos"
response = se.get(url)
print(response.text)
