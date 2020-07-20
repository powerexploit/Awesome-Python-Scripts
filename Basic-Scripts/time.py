import datetime as DT

time = DT.datetime.utcnow()
time = time.strftime("Year : %Y | Month : %B | WeekDay : %A | Hour : %H %p | Minute : %M | Second : %S ")
print(time)
