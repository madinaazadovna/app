#яша плавает в бассейне
N=int(input())
M=int(input())
x=int(input())
y=int(input())
if M>N:
    M, N= N, M
a=M-x
b=N-y
if a>x:
    c=x
else:
    c=a
if b>y:
    d=y
else:
    d=b
if c>d:
    print(d)
else:
    print(c)
