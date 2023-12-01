#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


def main():
    with request.urlopen(argv[1]) as response:
        if response.code != 200:
            print(f"Error code: {response.code}")
        else:
            response.read().decode("utf-8")


if __name__ == "__main__":
    main()
