#241
import datetime

print(datetime.datetime.now())

#242
import datetime

now = datetime.datetime.now()
print(now, type(now))

#243
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

