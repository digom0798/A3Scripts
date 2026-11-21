#Valores
Saldo_bancario = float(input("Qual o saldo bancário? "))
Valor_movimentar = float(input("Qual o valor a movimentar? "))

Saldo_atual = Saldo_bancario + Valor_movimentar

#Operação
if Saldo_atual <=0:
    print (f"Saldo inválido")
else:
    print(f"Saldo atual: {Saldo_atual}")
