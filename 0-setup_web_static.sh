#!/usr/bin/env bash
#create new dir and file to host hbnb_static
#changes ownership to ubuntu
#adds location element to /hbnb_static

mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

echo "Hello New file" > /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test /data/web_static/current 

chown -R ubuntu:ubuntu /data

sed -i '/.*internal.*/a \\t\tlocation /hbnb_static { alias /data/web_static/current; }' \
	/etc/nginx/sites-available/holberton

service nginx restart
