import datetime

today = datetime.date.today()
birth_date = datetime.date(2000, 1, 1)
times = today - birth_date
print("times:", times.days // 365)