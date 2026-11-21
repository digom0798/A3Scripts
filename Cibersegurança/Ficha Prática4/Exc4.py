while True:
#leitura dos numeros
    numero1 = float(input("Introduza o primeiro número: "))
    numero2 = float(input("Introduza o segundo número: "))

#leitura da operação
    operacao = input ("Introduza a operação (+, -, *, /): ")

#ciclo
    if operacao == "+":
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")

    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")

    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")

    elif operacao == "/":
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")

    else:
        print("Operação inválida")

    repetir = input ("Deseja continuar? (S/N): ")
    if repetir != "S":
        print ("Programa finalizado")
        break
