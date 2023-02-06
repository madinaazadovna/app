#Задача «Количество четных элементов последовательности»
a=0
while True:
    n=int(input())
    if n==0:
        break
    else:
        if n%2==0:
            a+=1
print(a)