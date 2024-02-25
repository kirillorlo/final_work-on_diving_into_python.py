from datetime import time, date, datetime
# d = date(year=2007, month=6, day=15)
# t = time(hour=2, minute=14, second=0, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
# second=0, microsecond=24)
# print(f'{d = }\t-\t{d}')
# print(f'{t = }\t-\t{t}')
# print(f'{dt = }\t-\t{dt}')

from datetime import time, date, datetime, timedelta
# d = date(year=2007, month=6, day=15)
# t = time(hour=2, minute=14, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
# microsecond=24)
# delta = timedelta(weeks=53, hours=73, minutes=101,
# seconds=303, milliseconds=60)
# print(f'{d.month}')
# print(f'{t.second}')
# print(f'{dt.hour}')
# print(f'{delta.days}')


# t = time(hour=2, minute=14, microsecond=24)
# dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
# microsecond=24)
# new_dt = dt.replace(year=2012)
# one_more_hour = t.replace(t.hour + 1)
# print(f'{new_dt}\n{one_more_hour}')

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14,
microsecond=24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))