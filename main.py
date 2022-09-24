from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction
)
import datetime
from message import(
    check_tesuto_onoff, schedule, kanji, tesuto,
    file, event_c, notice, feedback, change_file,change_notice, change_time,change_event,change_kanji,change_tesuto,change_tesuto_onoff,
    reset_monday_schedule,reset_tuesday_schedule,reset_wednesday_schedule,reset_thursday_schedule,reset_friday_schedule
)


app = Flask(__name__)

line_bot_api = LineBotApi('チャンネルアクセストークン')
handler = WebhookHandler('シークレットトークン')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 曜日
    weekday = datetime.date.today().weekday()
    # 時間
    now_time = int(datetime.datetime.now().strftime('%H'))
    
    now_time += 9
    if now_time > 24:
        now_time -= 24
        weekday += 1
        if weekday > 6:
            weekday = 0

    #入力メッセージ受け取り
    message = event.message.text
    if message == '時間割':
        message = schedule(weekday, now_time)
        line_bot_api.reply_message(
            event.reply_token,
            messages=message
        )

    elif message == '月曜日':
            line_bot_api.reply_message(
            event.reply_token,
            messages=schedule(0,6)
        )
    elif message == '火曜日':
            line_bot_api.reply_message(
            event.reply_token,
            messages=schedule(1,6)
        )
    elif message == '水曜日':
            line_bot_api.reply_message(
            event.reply_token,
            messages=schedule(2,6)
        )
    elif message == '木曜日':
            line_bot_api.reply_message(
            event.reply_token,
            messages=schedule(3,6)
        )
    elif message == '金曜日':
            line_bot_api.reply_message(
            event.reply_token,
            messages=schedule(4,6)
        )
    
    elif message == '範囲表':
        line_bot_api.reply_message(
            event.reply_token,
            messages = TemplateSendMessage(
                alt_text = "範囲",
                template = ButtonsTemplate(
                    title = "何の範囲を確認しますか？",
                    text = "定期テストの範囲表はテスト1週間前から利用可能です",            
                    image_size = "cover",
                    actions = [
                        MessageAction(
                        label = '漢字テスト',
                        text = '漢字テスト'
                        ),
                        MessageAction(
                        label = '定期テスト',
                        text = '定期テスト'
                        )
                    ]
                )
            )
        )

    elif message == '漢字テスト':
        message_content = kanji()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message_content
        )
    elif message == '定期テスト':
        active = check_tesuto_onoff()
        if active == '1':
            message_content = tesuto()
        elif active == '0':
            message_content = TextSendMessage(text='現在はテスト期間ではありません')
        line_bot_api.reply_message(
            event.reply_token,
            messages=message_content
        )

    elif message == '提出物':
        message_content = file()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message_content
        )
    elif message == '行事予定':
        message_content = event_c()
        line_bot_api.reply_message(
            event.reply_token,
             messages=message_content
        )
    elif message == 'お知らせ':
        message_content = notice()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message_content
        )
    elif message == '問い合わせ':
        message_content = feedback()
        line_bot_api.reply_message(
            event.reply_token,
            messages=message_content
        )
    #コマンド
    elif '@dev' in message:
        message_list = message.split(',')
        message_command = message_list[1]
        list_num = len(message_list)
        if message_command == '提出物':
            if list_num > 2:
                change_file(list_num, message_list)
                message = '提出物を変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == 'お知らせ':
            if list_num > 2:
                change_notice(list_num, message_list)
                message = 'お知らせを変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == '時間割':
            if list_num == 4  :
                change_time(message_list)
                message = '時間割を変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == '漢字':
            if list_num == 4:
                change_kanji(message_list)
                message = '漢字の範囲表を変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == 'テスト範囲':
            if list_num == 4:
                change_tesuto(message_list)
                message = '定期テストの範囲表を変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == '予定表':
            if list_num == 4:
                change_event(message_list)
                message = '予定表を変更しました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'

        elif message_command == 'テスト':
            if list_num == 2:
                change_tesuto_onoff()
                active = check_tesuto_onoff()
                if active == '0':
                    message='テスト期間をOFFにしました'
                elif active == '1':
                    message='テスト期間をONにしました'
            else:
                message = 'エラー:情報が不足しているか形式に誤りがあります'
                
        elif message_command == 'ヘルプ':
            message = \
'''
【@dev,】

・時間割,曜日番号(1~5),変更時間:変更科目-変更時間：変更科目...

・提出物,月日:内容,月日:内容...

・お知らせ,月日:内容,月日:内容...

・漢字,画像URL(1024px),画像URL(240px)

・予定表,画像URL(1024px),画像URL(240px)

・テスト範囲,画像URL(1024px),画像URL(240px)

・テスト(テスト期間の切り替え)

・リセット,曜日番号(全日:0/各日:1~5)
'''
        #時間割のリセット
        elif message_command == 'リセット':
            if list_num == 3:
                if message_list[2] == '0':
                    reset_monday_schedule()
                    reset_tuesday_schedule()
                    reset_wednesday_schedule()
                    reset_thursday_schedule()
                    reset_friday_schedule()
                    message = '全ての曜日の時間割をリセットしました'
                elif message_list[2] == '1':
                    message = reset_monday_schedule()
                elif message_list[2] == '2':
                    message = reset_tuesday_schedule()
                elif message_list[2] == '3':
                    message = reset_wednesday_schedule()
                elif message_list[2] == '4':
                    message = reset_thursday_schedule()
                elif message_list[2] == '5':
                    message = reset_friday_schedule()
                else:
                    message = '曜日ごとにリセットする場合は1~5、全ての曜日をリセットする場合は0を入力してください'
        

        #存在しないコマンドまたは間違ったコマンドが入力された場合
        else:
            message = 'エラー:情報が不足しているか形式に誤りがあります'

        line_bot_api.reply_message(
            event.reply_token,
            messages = TextSendMessage(text=message)
        )

    else:
        line_bot_api.reply_message(
            event.reply_token,
            messages = TextSendMessage(text='エラー')
        )

            
if __name__ == "__main__":
    app.run(debug=True)



'''
powershell
$env:FLASK_ENV = "development"
$env:FLASK_APP = "main"
flask run

cmd
set FLASK_ENV=development
set FLASK_APP=main
flask run
'''
