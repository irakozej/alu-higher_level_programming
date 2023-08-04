<<<<<<< HEAD
cript that:
=======
#!/usr/bin/python3
"""A script that:
>>>>>>> 8c392c40d3e8fcfcd561d0bc6aee21a3840791ab
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
