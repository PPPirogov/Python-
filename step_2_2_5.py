import datetime
year, month, day = map(int, input().split())
count = int(input())
a = datetime.date(year, month, day)+datetime.timedelta(count)
print(a.year, a.month, a.day)
