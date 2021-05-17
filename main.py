a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a > c:
    if a > b:
        maior = int(a)
        if b > c:
            medio = int(b)
            menor = int(c)
        else:
            medio = int(c)
            menor = int(b)
    else:
        maior = int(b)
        menor = int(c)
        medio = int(a)
else:
    if c > b:
        maior = c
        if a > b:
            medio = int(a)
            menor = int(b)
        else:
            medio = int(b)
            menor = int(a)
    else:
        maior = int(b)
        medio = int(c)
        menor = int(a)
print("{}\n{}\n{}\n".format(menor, medio, maior))
print("{}\n{}\n{}".format(a, b, c))