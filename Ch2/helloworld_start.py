#
# Example file for HelloWorld
#
import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def main(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://www.cracked.com")
print(r.status_code)
