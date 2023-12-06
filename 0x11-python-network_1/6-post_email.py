#!/usr/bin/python3
"""
Write a Python script that takes
in a URL and an email address, sends a POST request
"""
import requests
from sys import argv


def main():
    payload = {"email": argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response.text)


if __name__ == "__main__":
    main()
