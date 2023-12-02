#!/usr/bin/python3
"""
Display the variable X-Request-Id in the response header
"""
import requests as r
from sys import argv


def main():
    resp = r.get(argv[1])
    print(resp.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
