#!/bin/bash
# Send a GET request to a given URL with a header X-School-User-Id.
curl -sH "X-School-User-Id: 98" "${1}"
