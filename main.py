from urllib import request
import json
import subprocess

webhook_url = os.getenv('IP_NOTIFIR_WEBHOOK_URL')

command = 'curl global.me'

raw_result = subprocess.run(command.split(), stdout=subprocess.PIPE).stdout
result = raw_result.decode('utf-8').replace('\n', '')

main_content = json.dumps({
    'username': 'global IP notifier',
    'avatar_url': 'https://image.freepik.com/free-icon/ip-address_318-1438.jpg',
    'content': result
}).encode('utf-8')

headers = {'Content-Type': 'application/json'}

if not webhook_url:
    req = request.Request(webhook_url, data=main_conten, headers=headers,  method='POST')
