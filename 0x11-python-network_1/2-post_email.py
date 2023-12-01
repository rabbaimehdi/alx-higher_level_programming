#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


def main():
    query_params = parse.urlencode({'email': argv[2]}).encode("ascii")
    url = argv[1]
    with request.urlopen(request.Request(url, query_params)) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
