#ход короля
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if ((x2-x1==1) or (x2-x1==-1) or (x2-x1==0)) and ((y2-y1==1) or (y2-y1==-1) or (y2-y1==0)):
    print("YES")
else:
    print("NO")