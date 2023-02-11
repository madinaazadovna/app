#Задача «Количество нулей»
n=int(input())
a=0
for i in range(0,n):
    b=int(input())
    if(b==0):
        a+=1
print(a)