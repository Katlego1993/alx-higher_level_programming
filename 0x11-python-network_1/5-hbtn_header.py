#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""

import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
