#Leitura dos valores inteiros
valor1 = int (input("Introduza o primeiro valor inteiro (valor1): "))
valor2 = int (input("Introduza o segundo valor inteiro (valor2): "))

print(f"Antes da troca: valor1 = {valor1}, valor2 = {valor2}")

#Lógica matemática (troca de valores):
aux = valor1
valor1 = valor2
valor2 = aux

#Outra forma de calcular
#valor1 = valor1 + valor2
#valor2 = valor1 - valor2
#valor1 = valor1 - valor2

print(f"Após a troca: valor1 = {valor1}, valor2 = {valor2}")