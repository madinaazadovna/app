#Задача «Список квадратов»
n=int(input())
a=1
b=0
while n>b:
    b=a*a
    if n>=b:
        print(b," ")
    a+=1