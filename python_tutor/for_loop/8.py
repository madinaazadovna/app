#сумма факториалов
#Задача «Сумма факториалов»
sum=1
n=int(input())
a=1
s=0
for i in range(0,n):
    sum*=a
    a+=1
    s+=sum
print(s)