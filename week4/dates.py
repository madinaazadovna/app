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















