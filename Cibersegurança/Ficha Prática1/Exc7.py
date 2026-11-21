#Preço dos três produtos adquiridos
Produto1 = float(input("Introduza o valor do produto1: "))
Produto2 = float(input("introduza o valor do produto2: "))
Produto3 = float(input("Introduza o valor do produto3: "))

#Calculo subtotal dos produtos
Subtotal = Produto1 + Produto2 + Produto3

#Desconto sobre o valor do produto
Desconto = Subtotal * 0.10

#Calculo dos valores finais
Total = Subtotal - Desconto

#Apresentação de resultados
print(f"Subtotal: {Subtotal}")
print(f"Desconto: {Desconto}")
print(f"Total a pagar: {Total} €")