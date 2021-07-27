#!/usr/bin/env python3
from urllib import request
import json
import os

with open(os.path.dirname(__file__) + '/env.txt') as f:
    webhook_url = f.read()

ip_headers = {'User-Agent': 'curl'}

ip_request = request.Request('https://globalip.me', headers=ip_headers)
with request.urlopen(ip_request) as response:
    result = response.read().decode('utf-8')

content = json.dumps({
    'content': result,
}).encode('utf-8')

post_headers = {'User-Agent': 'curl', 'Content-Type': 'application/json'}

post_request = request.Request(webhook_url, data=content, headers=post_headers)
with request.urlopen(post_request) as response:
    body = response.read()
