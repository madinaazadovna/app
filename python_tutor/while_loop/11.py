#Задача «Количество элементов, которые больше предыдущего»
a=int(input())
i=0
while a!=0:
    b=int(input())
    if b!= 0 and a<b:
        i+=1
    a=b
print(i)
