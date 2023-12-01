#!/bin/bash
curl $1 -sI | grep Content-Length | grep -Po '\d+'
