import urllib
import json
import os

with open(os.path.dirname(__file__) + "/.env") as f:
    webhook_url = f.read()


def request(url, method, content=None):
    headers = {"User-Agent": "curl"}
    if method == "POST":
        headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, headers=headers, data=content, method=method)
    else:
        req = urllib.request.Request(url, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        if method == "POST":
            body = resp.read()
        else:
            return resp.read().decode("utf-8")


def main():
    ipaddress = request("https://globalip.me", "GET")
    content = json.dumps({"content": ipaddress}).encode("utf-8")
    request(webhook_url, method="POST", content=content)


if __name__ == "__main__":
    main()
