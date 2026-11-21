#variaveis
limite = int(input("Insira um numero inteiro (maior que 2): "))
numero = 2

while numero <= limite:
    if numero % 2 == 0:
        print(numero)
    numero = numero + 1
