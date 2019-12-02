"""

\t                    Tab
\\                    Inserts a back slash (\)
\'                    Inserts a single quote (')
\"                    Inserts a double quote (")
\n                    Inserts a ASCII Linefeed (a new line)

"""
#
#Display curent Python version on the console
from platform import python_version
print("Python " + python_version())
#
#
#Display curent time on console
import datetime
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#
#
#Display curent time on console (formatted)
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")