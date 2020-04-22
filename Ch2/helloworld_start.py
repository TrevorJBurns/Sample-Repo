#
# Example file for HelloWorld
#
import requests
import math


def main():
    r = requests.get("https://www.cracked.com")
    print(r.status_code)
    print(r.ok)
    print("Hello World")
