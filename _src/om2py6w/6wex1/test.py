import time
from datetime import date,timedelta, datetime
from time import sleep
now1 = time.time()
#now4 = time.ctime(now1)
#print now4 

#now2 = time.tzname 
#print now2

#sleep(1)

#now3 = time.localtime()
#now5 = time.asctime(now3)
#print now5

#now6 = time.ctime(now)
#timeStamp = 1448377666
#timeArray = time.localtime(timeStamp)
#print timeArray
#otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
#print otherStyleTime

#print timedelta(days=365)+timedelta(days=365)

#date1 = date.today()
#timedelta7 = timedelta(days=100)
#date2 = date1 + timedelta7
#date3 = date(2015, 12, 8)
#date4 = date3.strftime("%Y:%m:%d")

#d = datetime.today()

d = datetime.fromtimestamp(now1)
d2 = d.time()
d3 = d2.tzname()
print d3






