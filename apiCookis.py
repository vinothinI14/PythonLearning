import requests

url = "https://rahulshettyacademy.com/"
se = requests.session()
se.cookie= {'visit-month':'March'}

response = se.get(url,cookies ={'visit-year':'2024'},)
print(response.status_code)


