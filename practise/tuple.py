a = (1, 2, 3, 4)
b = tuple([3,4,5,6])
c = ("hello", 2, 3, 4, 4, False)
print(a, type(a))
print(b, type(b))
print(len(a))
print(2 in a, 7 in b)
print(a+b)
print(a*2)
print(max(b), min(a))
print(sum(a))
print(c[0])
print(a.index(3))
print(c.count(4))


d = [2, 4, 6, 7, False, [10, 20, 40]]
m = tuple([2, 4, 6, 7, False, [10, 20, 40]])
print(d.__sizeof__())
print(m.__sizeof__())


f = (3,4,5,56,7,8,9)
for i in range(len(f)) :
    print(f[i])
      
