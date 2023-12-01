#!/bin/bash
# display the size of the body response
curl $1 -sI | grep Content-Length | grep -Po '\d+'
