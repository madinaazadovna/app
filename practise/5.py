my_st = "Пример строки Python"
print(my_st.split())

my_st = "синий,оранжевый,красный"
print(my_st.split(","))

a = "this is sentence with something. And with commas and with some, thing else"
b = [str(s) for s in a.split()]
print(b)
c = [str(s) for s in a.split(".")]
print(c)
d = [str(s) for s in a.split(",")]
print(d)

a = "this is sentence with something. And with commas and with some, thing else"
print(a.split())
print(a.split(","))
print(a.split("."))

languages = "Python,Java,Perl,PHP,Swift"
print(languages.split(",",1))


languages = "This is no joke, this if njnsc jdnj"
lent = len(languages)//2
print(f"Первая половина: {languages[:lent]}")
print(f"Вторая половина:  {languages[lent:]}")
