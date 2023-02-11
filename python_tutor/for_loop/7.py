#Задача «Факториал»
sum=1
n=int(input())
a=1
for i in range(0,n):
    sum*=a
    a+=1
print(sum)