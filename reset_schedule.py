import schedule
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Gspread処理


#reset_schedule = f'【の時間割】\n1.\n2.\n3.\n4.\n5.\n6.'
def reset_monday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【月曜日の時間割】\n1.コ英/数Ⅲ\n2.英表/コ英\n3.発国/生物/物理/生物\n4.古文/化学\n5.日B/発数/発数\n6.弥生'
    worksheet.update_cell(2,1,reset_schedule)

def reset_tuesday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【火曜日の時間割】\n1.日B/発国/数Ⅲ\n2.古文/化学\n3.現文\n4.英表/コ英\n5.コ英/英表\n6.現社'
    worksheet.update_cell(2,2,reset_schedule)

def reset_wednesday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【水曜日の時間割】\n1.日B/発国/数Ⅲ\n2.発国/生物/物理/生物\n3.発国/生物/物理/生物\n4.体育\n5.古文/化学\n6.LHR'
    worksheet.update_cell(2,3,reset_schedule)

def reset_thursday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【木曜日の時間割】\n1.体育\n2.発数/美術/発国/数Ⅲ\n3.発数/美術/発数/英表\n4.発数/生物/物理/生物\n5.コ英/発数\n6.現文'
    worksheet.update_cell(2,4,reset_schedule)

def reset_friday_schedule():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('class-bot-347215-a4b263ffe581.json', scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = '128nXuzlxRSmhm7P1g0-tQC9rl3MSdVcHLF_2vp0ehpI'
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    reset_schedule = '【金曜日の時間割】\n1.コ英/発数\n2.現社\n3.発日/化学\n4.現文\n5.英表/コ英\n6.日B/発国/数Ⅲ'
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