# print("Hello, World!")
# print("Hello, Soumya!")

# importing 

import requests
response = requests.get("https://api.github.com")
print(response.status_code)
