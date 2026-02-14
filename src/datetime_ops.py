from datetime import datetime,date

print(datetime.now())
print(datetime.now().time())
print(datetime.now().date())
dt = datetime.now().date()
print(datetime.now().date().day)
print(dt.day)
print(dt.month)
print(dt.year)