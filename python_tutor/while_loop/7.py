#Задача «Среднее значение последовательности»
sum=0
i=0
while True:
    n=int(input())
    if n==0:
        break
    i+=1
    sum+=n
print(sum/i)