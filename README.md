# CLASS BOT_3.0

Procfileとrequirements.txtはHeroku用のファイルです。ローカル環境でテストする場合、下記のコマンドでライブラリはインストールしてください。

    $pip install -r requirements.txt
    
# チャンネルアクセストークンとシークレットトークン

main.pyの17行目,18行目にはLINE Messaging APIのチャンネルアクセストークンとシークレットトークンをそれぞれ入力してください。

## GCP

message.pyの10行目にはgcpのsheetsの鍵(json形式)のファイル名を入力してください。12行目には利用するシートのIDを入力してください。IDはURLにあります。「--/d/シートID/edit--」

# webhook URL

ローカル環境で実行する場合はngrokで5000番を開放しSSL化されたURLをLINE管理画面のwebhook URLに入力してください。URLの末に「/callback」と付けてください。サーバで運用するときはURLをwebhook URLに入力してください。こちらも同様に「/callback」と付け忘れないようにしてください。

# 仕様

## 時間割

午前9時以降・翌日午前9時までは翌日の時間割が表示されます。金曜日の午前9時以降から翌週月曜日の午前9時までは月曜日の時間割が表示されます。

## テストの範囲表

漢字テスト・ブライトステージ・定期テストの範囲表を確認することができます。現在ベータ版では漢字テストの範囲表が表示されません。また定期テストの範囲表は定期テスト１周間前から確認することができます。

## 提出物

何日に何を提出する必要があるのかを確認できます。これはクラス全体が提出するべき提出物のみ表示されます。各教科ごとの提出物については確認できません。

## 行事予定表

毎月の行事予定表を確認することができます。

## 使い方

BOTの使い方について確認することができます。他にもアカウントの「お知らせ」でも使い方を確認することができます。

## 質問・機能追加

BOTに間する質問や新しい機能の追加要望の問い合わせ先を確認することができます。表示されるLINEアカウントは僕(nao_kun)です。

## 管理者コマンド

BOTにはいくつかの管理者コマンドが存在します。管理者コマンドの一覧は「@dev,ヘルプ」と入力すれば確認することができます。