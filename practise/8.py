n = int(input())
i=2
min = 999999
while n>=i:
    if n%i==0:
        if i<=min:
            min=i
    i+=1
print(min)