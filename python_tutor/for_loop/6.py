#сумма кубов
#Задача «Сумма кубов»
n=int(input())
sum=0
a=1
for i in range(0,n,1):
    sum+=a**3
    a+=1
print(sum)