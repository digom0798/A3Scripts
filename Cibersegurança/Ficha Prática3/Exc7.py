#variaveis
numero = 1
limite = 100
soma = 0
#podemos tirar a variavel limite e colocar 100 diretamente no while

while numero <= limite:
    print(numero)
    soma = soma + numero
    numero = numero + 1

print (f"Somatorio: {soma}")
