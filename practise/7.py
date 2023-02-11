n = int(input())
len=0
while n > 0 :
    n//=10
    len+=1
print(len)