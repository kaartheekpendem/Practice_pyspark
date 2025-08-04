
from datetime import timedelta,datetime,date

print(datetime.now()- timedelta(5))
dt = datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)

a= '2025-08-01'
print(datetime.strptime(a,'%Y-%m-%d').day)