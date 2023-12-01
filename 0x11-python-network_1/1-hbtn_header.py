#!/usr/bin/python3
from urllib import request
from sys import argv

def main():
    with request.urlopen(argv[1]) as response:
        XRequestId = response.getheader('X-Request-Id')
        print(XRequestId)

if __name__ == "__main__":
    main()
