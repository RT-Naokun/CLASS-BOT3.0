from linebot.models import (
    TextSendMessage,  ImageSendMessage
)
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#<Gspread>
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = 'スプレッドシートID'
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#<メイン機能>
def schedule(weekday, now_time):
    #月曜日
    if weekday == 0:
        if now_time < 9:
            message_content = TextSendMessage(
                text = worksheet.cell(2,1).value
            )
            return message_content
    #火曜日
        else:
            message_content = TextSendMessage(
                text = worksheet.cell(2,2).value
            )
            return message_content
        
    elif weekday == 1:
        if now_time < 9:
            message_content = TextSendMessage(
                text = worksheet.cell(2,2).value
            )
            return message_content
    #水曜日
        else:
            message_content = TextSendMessage(
                text = worksheet.cell(2,3).value
            )
            return message_content

    elif weekday == 2:
        if now_time < 9:
            message_content = TextSendMessage(
                text = worksheet.cell(2,3).value
            )
            return message_content
    #木曜日
        else:
            message_content = TextSendMessage(
                text = worksheet.cell(2,4).value
            )
            return message_content
    elif weekday == 3:
        if now_time < 9:
            message_content = TextSendMessage(
                text = worksheet.cell(2,4).value
            )
            return message_content
    #金曜日
        else:
            message_content = TextSendMessage(
                text = worksheet.cell(2,5).value
            )
            return message_content

    elif weekday == 4:
        if now_time < 9:
            message_content = TextSendMessage(
                text = worksheet.cell(2,5).value
            )
            return message_content
    #月曜日
        else:
            message_content = TextSendMessage(
                text = worksheet.cell(2,1).value
            )
            return message_content

    elif weekday == 5:
        message_content = TextSendMessage(
            text = worksheet.cell(2,1).value
        )
        return message_content

    elif weekday == 6:
        message_content = TextSendMessage(
            text = worksheet.cell(2,1).value
        )
        return message_content

def kanji():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(6,2).value,
        preview_image_url=worksheet.cell(6,3).value
    )
    return message_content

def tesuto():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(7,2).value,
        preview_image_url=worksheet.cell(7,2).value
    )
    return message_content

def file():
    message_content = TextSendMessage(
        text=worksheet.cell(2,7).value
    )
    return message_content

def event_c():
    message_content = ImageSendMessage(
        original_content_url=worksheet.cell(9,2).value,
        preview_image_url=worksheet.cell(9,3).value
    )
    return message_content

def notice():
    message_content = TextSendMessage(
        text=worksheet.cell(2,8).value
    )
    return message_content

def feedback():
    message_content = TextSendMessage(
        text='3-2BOTに関する質問や新機能の要望などについてはメッセージで送信してください。'
    )
    return message_content

#<コマンド>
def change_file(list_num, message_list):
    base_text = '【提出物】\n'
    for n in range(list_num-2):
        change_file = message_list[n+2]
        if n < list_num-3:
            add_file = f'{change_file}\n'
        else:
            add_file = f'{change_file}'
        base_text = base_text + add_file
    worksheet.update_cell(2,7,base_text)

def change_notice(list_num, message_list):
    base_text = '【お知らせ】\n'
    for n in range(list_num-2):
        change_file = message_list[n+2]
        if n < list_num-3:
            add_file = f'{change_file}\n'
        else:
            add_file = f'{change_file}'
        base_text = base_text + add_file
    worksheet.update_cell(2,8,base_text)

def change_time(message_list):
    contents = message_list[3].split('-')
    week = int(message_list[2])
    now_schedule = worksheet.cell(2,week).value
    print(type(now_schedule))
    now_schedule = now_schedule.split('\n')
    #リストの内容を変更する時間割に修正
    for content in contents:
        content = content.split(':')
        num = int(content[0])
        subject = str(content[1])
        now_schedule[num] = f'{str(num)}.{subject}'
    update_schedule = ''
    #リストを文字列に変換
    for i in range(7):
        if i < 6:
            update_schedule += now_schedule[i]+'\n'
        else:
            update_schedule += now_schedule[i]
    worksheet.update_cell(2,week,update_schedule)

def change_kanji(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(6,2,list2)
    worksheet.update_cell(6,3,list3)

def change_tesuto(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(7,2,list2)
    worksheet.update_cell(7,3,list3)

def change_event(list):
    cut_list2 = list[2].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list2 = f'https://drive.google.com/uc?id={cut_list2}&.PNG'
    cut_list3 = list[3].replace('https://drive.google.com/file/d/','').replace('/view?usp=sharing','')
    list3 = f'https://drive.google.com/uc?id={cut_list3}&.PNG'
    worksheet.update_cell(9,2,list2)
    worksheet.update_cell(9,3,list3)

def change_tesuto_onoff():
    data = str(worksheet.cell(8,2).value)
    if data == '0':
        worksheet.update_cell(8,2,'1')
    elif data == '1':
        worksheet.update_cell(8,2,'0')
    else:
        worksheet.update_cell(8,2,'0')

#テスト期間かどうかを確認
def check_tesuto_onoff():
    return str(worksheet.cell(8,2).value)

#時間割リセット
def reset_monday_schedule():
    reset_schedule = '【月曜日の時間割】'
    worksheet.update_cell(2,1,reset_schedule)

    return '月曜日の時間割がリセットされました'

def reset_tuesday_schedule():
    reset_schedule = '【火曜日の時間割】'
    worksheet.update_cell(2,2,reset_schedule)

    return '火曜日の時間割がリセットされました'

def reset_wednesday_schedule():
    reset_schedule = '【水曜日の時間割】'
    worksheet.update_cell(2,3,reset_schedule)

    return '水曜日の時間割がリセットされました'

def reset_thursday_schedule():
    reset_schedule = '【木曜日の時間割】'
    worksheet.update_cell(2,4,reset_schedule)

    return '木曜日の時間割がリセットされました'

def reset_friday_schedule():
    reset_schedule = '【金曜日の時間割】'
    worksheet.update_cell(2,5,reset_schedule)

    return '金曜日の時間割がリセットされました'
