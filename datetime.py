from datetime import datetime

now = datetime.now().time().strftime("%H:%M:%S") # time object
date = datetime.now().strftime("%Y-%m-%d") # date object
print("date:",date) #o/p >> date: 2021-03-13
print("time =", now) #o/p >> time = 16:27:05
