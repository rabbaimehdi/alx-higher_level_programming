#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a
request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
from urllib import request
from sys import argv


def main():
    with request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    main()
