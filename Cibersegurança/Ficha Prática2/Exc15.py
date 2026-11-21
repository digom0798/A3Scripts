#Valores
Num1 = int(input("Introduza o primeiro numero: "))
Num2 = int(input("Introduza o segundo numero: "))
Num3 = int(input("Introduza o terceiro numero: "))

#Ordem escolhida
Ordem = input("Introduza a ordem que pretende (C) ou (D): ")
numeros = [Num1, Num2, Num3]

if Ordem == "C":
    numeros.sort()
    print(f"Números por ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")

elif Ordem == "D":
    numeros.sort(reverse=True)
    print(f"Números por ordem decrescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")

else:
    print("Opção Inválida")
