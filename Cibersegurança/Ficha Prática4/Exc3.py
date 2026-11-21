#Pedir ao utilizador
numero = int(input("Introduzir um número:"))

print(f"Divisores de {numero}:")

#ciclo
for i in range(1, numero +1):
    if numero % i == 0:
        print(i)
