#Valores do salário
Salario = int(input("Introduza o valor do salario:"))

#Calculo da taxa
if Salario <= 15000:
    Taxa = Salario * 0.2
    print(f"Taxa de 20%: {Taxa}€")
else:
    Taxa = Salario * 0.3
    print(f"Taxa de 30%: {Taxa}€")
