import datetime

start = datetime.datetime.now()
input()
finish = datetime.datetime.now()
time = (finish-start).total_seconds()
print(time)