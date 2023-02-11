#конец уроков
a=int(input())
t=0
for i in range(1, a):
    if i%2==0:
        t+=15
    else:
        t+=5
s=a*45
s+=t
a=(s//60) + 9
s=s%60
print(a,s)