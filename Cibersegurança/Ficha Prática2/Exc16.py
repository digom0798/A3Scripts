#Valores
Valor = int(input("Valor a levantar: "))

Notas = Valor // 200
print(f"Notas de 200€: {Notas}")
Valor = Valor % 200

Notas = Valor // 100
print(f"Notas de 100€: {Notas}")
Valor = Valor % 100

Notas = Valor // 50
print(f"Notas de 50€: {Notas}")
Valor = Valor % 50

Notas = Valor // 20
print(f"Notas de 20€: {Notas}")
Valor = Valor % 20

Notas = Valor // 10
print(f"Notas de 10€: {Notas}")
Valor = Valor % 10

Notas = Valor // 5
print(f"Notas de 5€: {Notas}")
Valor = Valor % 5
