#Задача «Максимум последовательности»
max=-1000
while True:
    n=int(input())
    if n==0:
        break
    else:
        if max<n:
            max=n
print(max)
