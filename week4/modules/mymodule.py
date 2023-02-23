"""Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application."""
def greeting(name):
  print ("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a)
#Create an alias for mymodule called mx:
import mymodule as mx
a = mx.person1["age"]
print(a)
