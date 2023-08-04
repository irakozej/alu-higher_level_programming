#!/usr/bin/python3


"""

Module to fetch and display the status from given URLs
"""

import urllib.request

def fetch_and_display_status(url):
    """
    Fetches the status from the given URL and displays the response body.
    Args:
        url (str): The URL to fetch the status from.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        content = content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    intranet_url = 'https://intranet.hbtn.io/status'
    local_url = 'http://0.0.0.0:5050/status'
    
    fetch_and_display_status(intranet_url)
    fetch_and_display_status(local_url)

