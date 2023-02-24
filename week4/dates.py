#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
#Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

#Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

"""To create a date, we can use the datetime() class (constructor) of the datetime module.
datetime()The class requires three parameters to create a date: year, month, day."""
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#Weekday, short version
import datetime
x = datetime.datetime.now()
print(x.strftime("%a")) #answer: Thu

#Weekday, full version
import datetime
x = datetime.datetime.now()
print(x.strftime("%A")) #answer: Thursday

#Weekday as a number 0-6, 0 is Sunday
import datetime
x = datetime.datetime.now()
print(x.strftime("%w")) #answer: 4

#Day of month 01-31
import datetime
x = datetime.datetime.now()
print(x.strftime("%d")) #answer: 23

#Month name, short version
import datetime
x = datetime.datetime.now()
print(x.strftime("%b")) #answer: Feb

#Month name, full version
import datetime
x = datetime.datetime.now()
print(x.strftime("%w")) #answer: 4

#Month as a number 01-12
import datetime
x = datetime.datetime.now()
print(x.strftime("%m")) #answer: 02

#Year, short version, without century
import datetime
x = datetime.datetime.now()
print(x.strftime("%y")) #anser: 23

#Year, full version
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y")) #answer: 2023

#Hour 00-23
import datetime
x = datetime.datetime.now()
print(x.strftime("%H")) #answer: 16

#Hour 00-12
import datetime
x = datetime.datetime.now()
print(x.strftime("%I")) #answer: 04

#AM/PM
import datetime
x = datetime.datetime.now()
print(x.strftime("%p")) #answer: pm

#Minute 00-59
import datetime
x = datetime.datetime.now()
print(x.strftime("%M")) #answer: 18

#Second 00-59
import datetime
x = datetime.datetime.now()
print(x.strftime("%S")) #answer: 11

#Microsecond 000000-999999
import datetime
x = datetime.datetime.now()
print(x.strftime("%f")) #answer: 952187

#Day number of year 001-366
import datetime
x = datetime.datetime.now()
print(x.strftime("%j")) #answer: 55

#Week number of year, Sunday as the first day of week, 00-53
import datetime
x = datetime.datetime.now()
print(x.strftime("%U")) #answer: 21

#Week number of year, Monday as the first day of week, 00-53
import datetime
x = datetime.datetime(2018, 5, 31)
print(x.strftime("%W")) #answer: 22

#Local version of date and time
import datetime
x = datetime.datetime.now()
print(x.strftime("%c")) #answer: Fri Feb 24 14:22:05 2023

#Century
import datetime
x = datetime.datetime.now()
print(x.strftime("%C")) #answer: 20

#Local version of date
import datetime
x = datetime.datetime.now()
print(x.strftime("%x")) #answer: 02/24/23

#Local version of time
import datetime
x = datetime.datetime.now()
print(x.strftime("%X")) #answer: 14:25:16

#A % character
import datetime
x = datetime.datetime.now()
print(x.strftime("%%")) #answer: %

#ISO 8601 year
import datetime
x = datetime.datetime.now()
print(x.strftime("%G")) #answer: 2023

#ISO 8601 weekday (1-7)
import datetime
x = datetime.datetime.now()
print(x.strftime("%u")) #answer: 5

#ISO 8601 weeknumber (01-53)
import datetime
x = datetime.datetime.now()
print(x.strftime("%V")) #answer: 08




























