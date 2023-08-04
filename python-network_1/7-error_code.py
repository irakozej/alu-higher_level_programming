<<<<<<< HEAD
cript that
=======
#!/usr/bin/python3
"""A script that
>>>>>>> 8c392c40d3e8fcfcd561d0bc6aee21a3840791ab
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
