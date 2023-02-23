#Now we can use the module we just created, by using the import statement:
#Import the module named mymodule, and call the greeting function:
import mymodule
mymodule.greeting("Jonathan")

#Import and use the platform module:
import platform
x = platform.system()
print(x)

#There is a built-in function to list all the function names (or variable names) in a module. The dir():
import platform
x = dir(platform)
print(x)

#Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"])
