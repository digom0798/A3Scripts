numero = int(input("Introduza um número inteiro positivo: "))

if numero < 1:
    print("Por favor, introduza um número natural (maior que 0):")
elif numero == 1:
    print("O número 1 é primo.")
else:
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1
    if divisores == 2:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo (tem {divisores} divisores)")
