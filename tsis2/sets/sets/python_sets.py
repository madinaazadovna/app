#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) 

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) 

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))  

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1) 
print(set2)  
print(set3)  

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print(set1)  

#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))   

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) 
print(thisset)  