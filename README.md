# discord-ip-notifier

cronを使って1時間ごとにRPiのグローバルIPアドレスをdiscordに送信するプログラム

## Usage

`env.txt`にwebhookのURLを書く

```:env.txt
https://discord.com/api/webhooks/1234567890/hogehoge
```

`crontab`に以下の設定を書く

```crontab
* */1 * * * cd /path/to/discord-ip-notifier; ./main.py
```
