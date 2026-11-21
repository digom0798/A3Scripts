#Valores
Num1 = int(input("Introduza um numero inteiro: "))
Num2 = int(input("Introduza outro numero inteiro: "))
NUm3 = int(input("Introduza outro numero inteiro: "))

numeros = [Num1, Num2, NUm3]

#Ordem Crescente
numeros.sort()

#Resultados
print(f"Números por ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")