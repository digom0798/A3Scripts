#variaveis
inserir = int(input("Quantos numeros deseja inserir? "))
contador = 1
crescente = True

numero_anterior = int(input("Insira o numero: "))

#formula
while contador < inserir:
    numero_atual = int(input("Insira o numero: "))

    if numero_atual < numero_anterior:
        crescente = False

    numero_anterior = numero_atual
    contador = contador + 1

#resultado
if crescente:
    print("A sequencia está em ordem crescente")
else:
    print("A sequencia nao esta em ordem crescente")