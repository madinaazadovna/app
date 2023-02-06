#Задача «Индекс максимума последовательности»
max=-1000
b=0
i=0
while True:
    n=int(input())
    if n==0:
        break
    else:
        if max<n:
            max=n
            b=i
    i+=1
print(b)