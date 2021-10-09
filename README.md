# discord-ip-notifier

docker + cronを使って1時間ごとにRPiのグローバルIPアドレスをdiscordに送信するプログラム

## Usage

`.env`(`main.py`と同階層)にwebhookのURLを書く

```.env
https://discord.com/api/webhooks/1234567890/hogehoge
```

イメージをbuildして起動

```shell
docker build . -t "$(basename $PWD)"
docker run -itd --rm --name "$(basename $PWD)" "$(basename $PWD)"
```
