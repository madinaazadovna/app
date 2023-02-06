#Задача «Потерянная карточка»
n=int(input())
a=n
b=0
for i in range(1,n):
    a+=i
    b+= int(input())
print(a-b)
