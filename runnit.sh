#!/bin/sh
docker rm fakefinch
docker build -t fakefinch .
docker run --name fakefinch -p 800:800 fakefinch -d