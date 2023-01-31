#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)  

#Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)  

#Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)  

#Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)  

#Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

#Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)  

#Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)  

#Delete the element that has the value "Volvo":
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)  


