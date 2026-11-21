#variaveis
inicio = int(input("Digite um numero inteiro inicio: "))
limite = int(input("Digite um numero inteiro fim: "))
numero = inicio

#formula
while numero <= limite:
    if numero % 5 == 0:
        print(numero)
    numero = numero + 1
