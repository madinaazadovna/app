#шоколадка
a = int(input())
b = int(input())
c = int(input())
if c%a==0 and a*b>=c:
    print("YES")
elif c%b==0 and a*b>=c:
    print("YES")
else:
    print("NO")