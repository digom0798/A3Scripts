#variaveis
numero = int(input("Insira um número (-1 para terminar): "))
soma = 0
contador = 0

#formula
while numero != -1:
    soma = soma + numero
    contador = contador + 1
    numero = int(input("insira um número (-1 para terminar): "))

if contador > 0:
    media = soma / contador
    print("Média: ", media)
else:
    print("Nenhum número válido inserido.")
