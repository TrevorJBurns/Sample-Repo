#
# Example file for HelloWorld
#
import requests

r = requests.get("https://www.cracked.com")
print(r.status_code)
print(r.ok)
