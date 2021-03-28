import math
import os
import sys

import requests

print(sys.executable)
r = requests.get("https://google.com")
print(r.status_code)
