#Задача «Лесенка»
n=int(input())
a=1.23456789
for i in range(n):
    if i==8:
        print(123456789)
    else:
        print(int(a*10**i))