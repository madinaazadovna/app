"""JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation."""
#Python has a built-in package called json, which can be used to work with JSON data.

#Convert from JSON to Python:
import json
# some JSON:
x = { "name":"John", "age":30, "city":"New York"}
y = json.loads(x)
print(y["age"])

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)

#Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a Python object containing all the legal data types:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)
print(y)

#Use the indent parameter to define the numbers of indents:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))

#Use the separators parameter to change the default separator:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Use the sort_keys parameter to specify if the result should be sorted or not:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

