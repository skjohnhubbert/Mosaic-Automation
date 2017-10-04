from datetime import datetime, timedelta, date
from time import strftime

today_1 = datetime.today()
start_date_2 = today_1.replace(day=8, month=8, year=2017)
today = today_1.strftime('%m/%d/%Y')
start_date = start_date_2.strftime('%m/%d/%Y')

while True:
    today > start_date
    today = today_1 - timedelta(days = 1)
    today = today.strftime('%m/%d/%Y')
    print(today)
    if today == start_date:
        break
