from random import randint
c = "bcdfghjklmnpqrstvwxyz"
v = "aeiou"
for i in range(0, randint(2, 3)):
    print(c[randint(0, len(c)-1)], end="")
    print(v[randint(0, len(v)-1)], end="")