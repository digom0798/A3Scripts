#Valores
Numero1 = int(input("Escreve um número inteiro aqui: "))
Numero2 = int(input("Escreve um número inteiro aqui: "))

Operaçao = input("Escolha a operação (+, -, *, /): ")

#Operações aritméticas
if Operaçao == '+':
    Resultado = Numero1 + Numero2
    print (f"Resultado: {Numero1} + {Numero2} = {Resultado} ")

elif Operaçao == '-':
    Resultado = Numero1 - Numero2
    print (f"Resultado: {Numero1} - {Numero2} = {Resultado} ")

elif Operaçao == '*':
    Resultado = Numero1 * Numero2
    print (f"Resultado: {Numero1} * {Numero2} = {Resultado} ")

elif Operaçao == '/':
    Resultado = Numero1 / Numero2
    print (f"Resultado: {Numero1} / {Numero2} = {Resultado} ")

else:
    print (f"Erro: Operação não reconhecida")
