numerolido = int(input("Digite um numero: "))
inicio = numerolido - 5
fim = numerolido + 5

numero = inicio

#formula
while numero <= fim:
    if numero != numerolido:
        print(numero)
    numero = numero + 1

#Outra forma de resolver
# 5 anteriores
numero = numerolido - 5
limite = numerolido - 1

while numero <= limite:
    print(numero)
    numero = numero + 1

# 5 sucessores
numero = numeroligo + 1
limite = numerolido + 5

while numero <= limite:
    print(numero)
    numero = numero + 1