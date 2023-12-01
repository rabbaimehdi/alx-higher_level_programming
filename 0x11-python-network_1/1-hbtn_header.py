#!/usr/bin/python3
from urllib import request
from sys import argv


def main():
    with request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    main()
