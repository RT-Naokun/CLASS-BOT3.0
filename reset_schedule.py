import schedule
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Gspread処理


#reset_schedule = f'【の時間割】\n1.\n2.\n3.\n4.\n5.\n6.'
def reset_monday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = 'スプレッドシートID'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【月曜日の時間割】\n1.コ英/数Ⅲ\n2.英表/コ英\n3.発国/生物/物理/生物\n4.古文/化学\n5.日B/発数/発数\n6.弥生'
    worksheet.update_cell(2,1,reset_schedule)

def reset_tuesday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = 'スプレッドシートID'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【火曜日の時間割】'
    worksheet.update_cell(2,2,reset_schedule)

def reset_wednesday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = 'スプレッドシートID'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【水曜日の時間割】'
    worksheet.update_cell(2,3,reset_schedule)

def reset_thursday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = 'スプレッドシートID'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【木曜日の時間割】'
    worksheet.update_cell(2,4,reset_schedule)

def reset_friday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('jsonファイル', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = 'スプレッドシートID'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【金曜日の時間割】'
    worksheet.update_cell(2,5,reset_schedule)


#平日10:00に各曜日の時間割をリセットする
schedule.every().monday.at('01:00').do(reset_monday_schedule)
schedule.every().tuesday.at('01:00').do(reset_tuesday_schedule)
schedule.every().wednesday.at('01:00').do(reset_wednesday_schedule)
schedule.every().thursday.at('01:00').do(reset_thursday_schedule)
schedule.every().friday.at('01:00').do(reset_friday_schedule)

while True:
    schedule.run_pending()
    sleep(1)
