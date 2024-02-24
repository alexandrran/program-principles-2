# Exercise 1
import datetime
x = datetime.datetime.now()
b = datetime.datetime(x.year, x.month, x.day - 5)
print(b.strftime("%x"))

# Exercise 2
import datetime
x = datetime.datetime.now()
yesterday = datetime.datetime(x.year, x.month, x.day - 1)
tomorrow = datetime.datetime(x.year, x.month, x.day + 1)
print("Yesterday:", yesterday.strftime("%A"))
print("Today: ", x.strftime("%A"))
print("Tomorrow: ", tomorrow.strftime("%A"))

# Exercise 3
import datetime
current_datetime = datetime.datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(f"Текущее время без микросекунд: {datetime_without_microseconds}")

# Exercise 4
import datetime

a = datetime.datetime(2023,12,30,23,59,59)
b = datetime.datetime(2023,12,31,23,59,59)

print((b-a).total_seconds())
