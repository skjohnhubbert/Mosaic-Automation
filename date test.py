from datetime import datetime, timedelta, date
from time import strftime

today = datetime.today()
start_date = today.replace(day=8, month=8, year=2017)

while True:
    if today > start_date:
        today = today - timedelta(days = 1)
        today_strftime = today.strftime('%m/%d/%Y')
        print(today_strftime)
    if today == start_date:
        break
