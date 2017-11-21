#!/usr/bin/env bash
# Setup new location block for `/hbnb_static`

# create directories
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

# add test string 
echo "Hello New file" > /data/web_static/releases/test/index.html

# create a soft link with test -> current
ln -fs /data/web_static/releases/test /data/web_static/current 

# give full ownership of all files in data dir
chown -R ubuntu:ubuntu /data

# add new location to URI to point to the softlink current
sed -i '/.*internal.*/a \\t\tlocation /hbnb_static { alias /data/web_static/current; }' \
	/etc/nginx/sites-available/holberton

service nginx restart
