from datetime import datetime
now = datetime.now()
m = str(now.month)
d = str(now.day)
y = str(now.year)
hr = str(now.hour)
min = str(now.min)
s = str(now.second)
print( m + "-" + d + "-" + y + " " + hr + ":" + min + ":" + s )
