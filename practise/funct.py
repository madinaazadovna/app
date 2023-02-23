def funct(fname):
    print(fname + " Hello")

funct("Emil")
funct("Madina")
funct("Mukanova")


def multiple(a, b):
    product = a*b
    return(int(product))

print(multiple(3, 4))

def calculate(num1, num2):
    return num1 + num2, num1*num2, num1*num2

res1, res2, res3 = calculate(5, 6)
print(res1, res2, res3)