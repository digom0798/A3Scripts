#Valores
Num1 = int(input("Escreve aqui um número inteiro: "))
Num2 = int(input("Escreve aqui um número inteiro: "))
Num3 = int(input("Escreve aqui um número inteiro: "))

#Calular o menor
if Num1 < Num2 and Num1 < Num3:
    print (f"O menor número é {Num1}")
elif Num2 < Num3:
    print (f"O menor número é {Num2}")
else:
    print (f"O menor número é {Num3}")
