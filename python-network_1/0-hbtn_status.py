#!/usr/bin/python3
"""
Module to fetch and display the status from https://alu-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content = content.decode('utf-8')
    
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
