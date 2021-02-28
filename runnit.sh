#!/bin/sh
docker rm fakefinch
docker build -t fakefinch .
docker run -d --name fakefinch -p 800:800 fakefinch