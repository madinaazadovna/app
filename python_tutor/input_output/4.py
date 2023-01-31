#электронные часы

n=int(input())
s=n//60
m=n-s*60
k=s//24
if s<24:
    print(s,m)
else:
    print(s-24*k,m)