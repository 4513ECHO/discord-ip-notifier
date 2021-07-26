# discord-ip-notifier

systemdを使って1時間ごとにRPiのグローバルIPアドレスをdiscordに送信するプログラム

## Usage

### 準備

```shell
IP_NOTIFIER_WEBHOOK_URL=https://discord.com/api/webhook/1234567890/hogehoge
```

```shell
sudo systemctl link /home/hibiki/Develops/discord-ip-notifier/notifier.service
sudo systemctl link /home/hibiki/Develops/discord-ip-notifier/notifier.timer
sudo systemctl enable /home/hibiki/Develops/discord-ip-notifier/notifier.service
sudo systemctl enable /home/hibiki/Develops/discord-ip-notifier/notifier.timer
```

### 起動/停止

```shell
sudo systemctl start notifier
sudo systemctl stop notifer
```
