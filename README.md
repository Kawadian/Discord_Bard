# README

## DiscordでBardを使用するためのPythonスクリプトの使い方

このPythonスクリプトは、Discordの特定のチャンネルでメッセージを受信したとき、または直接メッセージやメンションを受信したときに、Bardを利用して自動的に応答します。

### 必要なもの
- Python3
- Discordボットのトークン
- BardのAPIキー

### インストール

Pythonが既にインストールされていることを確認します。次に、以下のコマンドを実行して必要なライブラリをインストールします。

```
pip install discord.py bardapi
```

### 使用方法

1. まず、Discord botとBardのAPIキーを取得します。
Chromeを使用して以下のURLを開き、Bardを起動します。
https://bard.google.com/
F12を押して、アプリケーション→cookie→__Secure-1PSIDの順に進み、値をコピーしておきます。

2. Pythonスクリプトに、Discord botのトークンとBardのAPIキーを記入します。

   ```python
   bard_token = 'your-bard-api-key' 
   client.run("your-discord-bot-token")
   ```

3. `target_channel_ids` のリストに、監視したいDiscordチャンネルのIDを追加します。

   ```python
   target_channel_ids = [1112563855852314674, 1112630941572141077, 12345]
   ```

4. すべての設定が完了したら、Pythonスクリプトを実行します。

   ```
   python your-script.py
   ```

ボットが起動したら、指定されたDiscordチャンネルでメッセージを送信するか、ボットに直接メッセージを送信するか、メンションすると、自動的に応答します。注意すべき点として、ボットは他のボットからのメッセージには応答しません。

### 注意事項

- BardのAPIキーとDiscordのボットのトークンはとても重要です。絶対に他人に見られないようにしてください。それらはあなたのアカウントを制御するためのキーであり、それらを知られてしまうとあなたのアカウントが不正に利用される可能性があります。

- このスクリプトはサンプルであり、使用する際には適切なエラーハンドリングやセキュリティ対策を実装することを強く推奨します。

以上がこのPythonスクリプトの基本的な使い方です。詳細についてはDiscord botやBardapiの公式ドキュメンテーションを参照してください。
参考：https://github.com/dsdanielpark/Bard-API
