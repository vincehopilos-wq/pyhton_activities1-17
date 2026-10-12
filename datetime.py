from datetime import date,datetime

today = date.today
now = datetime.now()

print("current date", today)
print("current year", today.year)
print("current month", today.month)
print("current day", today.day)
print("current hour", now.hour)