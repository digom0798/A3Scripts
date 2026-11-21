# Notas
nota1 = float(input("Introduzir o valor da primeira nota: "))
nota2 = float(input("Introduzir o valor da segunda nota: "))
nota3 = float(input("introduzir o valor da terceira nota: "))

# Calculo da media aritmetica
media_aritmetica = (nota1 + nota2 + nota3) / 3

#Calculo da media ponderada
#20% = 0.20 / 30% = 0.30 / 50% = 0.50
media_ponderada = (nota1 * 0.20) + (nota2 * 0.30) + (nota3 * 0.50)

#Apresentação de resultados
print(f"Media aritmetica: {media_aritmetica}")
print(f"Media ponderada: {media_ponderada}")
