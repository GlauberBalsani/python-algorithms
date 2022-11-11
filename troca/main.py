x = int(input(": "))
y = int(input(": "))

print('Variavel x', x)
print('Variavel Y ', y)
print()


if x > y:
    print("Invertendo..")
    aux = y
    y = x
    x = aux
else:
    print("Não precisa inverter")

print(x)
print(y)
    

