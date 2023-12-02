#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    body = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response")
    print(f"\t- type: {type(body.content)}")
    print(f"\t- content: {body.content}")


if __name__ == "__main__":
    main()
