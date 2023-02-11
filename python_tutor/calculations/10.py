#число десятков
import math
n=int(input())
if n>=100:
    a=n//100
    b=n-a*100
    print(b//10)
else:
    print(n//10)