#Задача «Второй максимум»
max=-1000
smax=-1000
while True:
    n=int(input())
    if n==0:
        break
    else:
        if max<n:
            smax=max
            max=n
        elif n>smax:
            smax=n
print(smax)