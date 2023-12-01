#!/usr/bin/python3
from urllib import request
with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
	print(response.read().decode('UTF-8'))
