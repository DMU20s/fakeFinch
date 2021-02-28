#!/bin/sh
git pull
docker rm fakefinch
docker build -t fakefin .
docker run --name fakefinch -p 800:800 fakefinch -d