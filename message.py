from linebot.models import (
    TextSendMessage, TemplateSendMessage, MessageAction, ButtonsTemplate, ImageSendMessage
)
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Gspread処理
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#時間割
def schedule(weekday, now_time):
    #月曜日
    if weekday == 0:
        if now_time < 9:
            monday = worksheet.cell(2,1).value
            message_content = TextSendMessage(
                text=monday
            )
            return message_content
        #火曜日
        else:
            tuesday = worksheet.cell(2,2).value
            message_content = TextSendMessage(
                text=tuesday
            )
            return message_content
        
    elif weekday == 1:
        if now_time < 9:
            tuesday = worksheet.cell(2,2).value
            message_content = TextSendMessage(
                text=tuesday
            )
            return message_content
        #水曜日
        else:
            wednesday = worksheet.cell(2,3).value
            message_content = TextSendMessage(
                text=wednesday
            )
            return message_content

    elif weekday == 2:
        if now_time < 9:
            wednesday = worksheet.cell(2,3).value
            message_content = TextSendMessage(
                text=wednesday
            )
            return message_content
        #木曜日
        else:
            thursday = worksheet.cell(2,4).value
            message_content = TextSendMessage(
                text=thursday
            )
            return message_content
    elif weekday == 3:
        if now_time < 9:
            thursday = worksheet.cell(2,4).value
            message_content = TextSendMessage(
                text=thursday
            )
            return message_content
        #金曜日
        else:
            friday = worksheet.cell(2,5).value
            message_content = TextSendMessage(
                text=friday
            )
            return message_content

    elif weekday == 4:
        if now_time < 9:
            friday = worksheet.cell(2,5).value
            message_content = TextSendMessage(
                text=friday
            )
            return message_content
        else:
            monday = worksheet.cell(2,1).value
            message_content = TextSendMessage(
                text=monday
            )
            return message_content

    elif weekday == 5:
        monday = worksheet.cell(2,1).value
        message_content = TextSendMessage(
            text=monday
        )
        return message_content

    elif weekday == 6:
        monday = worksheet.cell(2,1).value
        message_content = TextSendMessage(
            text=monday
        )
        return message_content

#範囲
def scope():
    message_content = TemplateSendMessage(
        alt_text="範囲",
        template=ButtonsTemplate(
            title="何の範囲を確認しますか？",
            text="定期考査の範囲表は考査1週間前に更新します",            
            image_size="cover",
            actions=[
                MessageAction(
                label='漢字テスト',
                text='漢字テスト'
                ),
                MessageAction(
                label='ブライトステージ',
                text='ブライトステージ'
                ),
                MessageAction(
                label='定期テスト',
                text='定期テスト'
                )
            ]
        )
    )
    return message_content

#コマンド
def change_file(message_command, list_num, message_list):
    if message_command == '提出物':
        base_text = '【提出物】\n'
        for n in range(list_num-2):
            change_file = message_list[n+2]
            if n < list_num-3:
                add_file = f'{change_file}\n'
            else:
                add_file = f'{change_file}'
            base_text = base_text + add_file
        worksheet.update_cell(2,7,base_text)

#時間割変更
def change_time(message_list):
    contents = message_list[3]
    contents = contents.split('-')
    week = int(message_list[2])
    now_schedule = worksheet.cell(2,week)
    now_schedule = str(now_schedule).replace(f"<Cell R2C{week} '","").replace("'>","")
    now_schedule = now_schedule.split('\n')
    now_schedule = now_schedule[0].split('.')
    for i,now in enumerate(now_schedule):
        now = now.replace('\\n','\n')
        now_schedule[i] = now
    for content in contents:
        content = content.split(':')
        num = int(content[0])
        subject = str(content[1])
        next_num = num + 1            
        now_schedule[num] = f'{subject}\n{str(next_num)}'
    update_schedule = ''
    for i in range(7):
        if i == 6:
            if '7' in now_schedule[6]:
                now_schedule[6] = now_schedule[6].replace('\n7','')
        update_schedule += now_schedule[i]+'.'
    worksheet.update_cell(2,week,update_schedule)

def change_kanji(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','')
    cut_list2 = cut_list2.replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','')
    cut_list3 = cut_list3.replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(6,2,list2)
    worksheet.update_cell(6,3,list3)

def change_bright(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','')
    cut_list2 = cut_list2.replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','')
    cut_list3 = cut_list3.replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(7,2,list2)
    worksheet.update_cell(7,3,list3)

def change_tesuto(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','')
    cut_list2 = cut_list2.replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','')
    cut_list3 = cut_list3.replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(8,2,list2)
    worksheet.update_cell(8,3,list3)

def change_event(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','')
    cut_list2 = cut_list2.replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','')
    cut_list3 = cut_list3.replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(10,2,list2)
    worksheet.update_cell(10,3,list3)

def change_tesuto_onoff():
    data = str(worksheet.cell(9,2).value)
    if data == '0':
        worksheet.update_cell(9,2,'1')
    elif data == '1':
        worksheet.update_cell(9,2,'0')
    else:
        worksheet.update_cell(9,2,'0')

def check_tesuto_onoff():
    return str(worksheet.cell(9,2).value)


'''
画像のフォーマット
https//drive.google.com/uc?id={id}&.{拡張子}
'''

def kanji():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(6,2).value,
        preview_image_url=worksheet.cell(6,3).value
    )
    return message_content

def brightstage():
    message_content = ImageSendMessage(
        original_content_url = worksheet.cell(7,2).value,
        preview_image_url = worksheet.cell(7,3).value
    )
    return message_content

def tesuto():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(8,2).value,
        preview_image_url=worksheet.cell(7,2).value
    )
    return message_content

def file():
    base_text = worksheet.cell(2,7).value
    message_content = TextSendMessage(
        text=base_text
    )
    return message_content

def event_c():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(10,2).value,
        preview_image_url=worksheet.cell(10,3).value
    )
    return message_content

#others
def information():
    message_content = TextSendMessage(
        text='【使い方】\n 文字入力不要の『らくらくメニュー』を使って、欲しい情報をタップするだけ！\n 他に分からないことや新しい機能の要望があれば"Feedback(質問・機能追加)"をタップ'
    )
    return message_content

def feedback():
    message_content = TextSendMessage(
        text='3-2BOTに関する質問や新しい機能に関する要望は開発者にご連絡ください。\n https://line.me/ti/p/XCAi0yQ5VA'
    )
    return message_content
