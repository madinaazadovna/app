#сколько совпадает чисел

a = int(input())
b = int(input())
c = int(input())
if (a == b and b == c) :
    print('3')
elif(a==b and a!=c):
    print('2')
elif(a!=b and b ==c):
    print('2')
elif(a!=b and a==c):
    print('2')
elif(a!=b and a!=c):
    print('0')