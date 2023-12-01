#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
from urllib import request, error
from sys import argv


def main():
    try:
        with request.urlopen(argv[1]) as response:
            print(request.read().decode("ascii"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
