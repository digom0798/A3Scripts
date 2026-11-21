#Valores do salário
Salario = int(input("Introduza o valor do salario:"))

#Salário até 15.000€ inclusive paga taxa de 20%
if Salario <= 15000:
    Taxa = Salario * 0.2
    print(f"Taxa de 20%: {Taxa}€")

#Salário de 15.000€ a 20.000€ inclusive paga taxa de 30%
if Salario > 15000 and Salario <= 20000:
    Taxa = Salario * 0.3
    print(f"Taxa de 30%: {Taxa}")

#Salário de 20.000€ a 25.000€ inclusive paga taxa de 35%
if Salario > 20000 and Salario <= 25000:
    Taxa = Salario * 0.35
    print(f"Taxa de 35%: {Taxa}")

#Salário superior a 25.000€ paga taxa de 40%
if Salario > 25000:
    Taxa = Salario * 0.40
    print(f"Taxa de 40%: {Taxa}")
