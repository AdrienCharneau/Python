#
import datetime
#
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#
#
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")