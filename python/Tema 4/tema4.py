Lista =[]

for numero in range(1, 101):
    Lista.append(numero)
    Lista = list(range(100, 0, -1))

print(Lista)

#or

rango_1_100 = range(1,101)
for i in reversed(rango_1_100):
    print(f"- {i}")
