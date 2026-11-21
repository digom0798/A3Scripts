# variaveis
numero = int(input("Digite aqui o numero inteiro nao-negativo: "))
contador = numero
fatorial = 1

#formula
while contador > 1:
    fatorial = fatorial * contador
    contador = contador -1

#resultado
print(f"Fatorial de {numero}: {fatorial}")