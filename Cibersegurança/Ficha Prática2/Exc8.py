#Valores das notas
Nota1 = float(input("Escreve o valor da primeira nota: "))
Nota2 = float(input("Escreve o valor da segunda nota: "))
Nota3 = float(input("Escreve o valor da terceira nota: "))

#Calculo da média ponderada
Media_Ponderada = (Nota1 * 0.25) + (Nota2 * 0.35) + (Nota3 * 0.40)

#Resultados
print (f"Média Ponderada: {Media_Ponderada}")

#Aprovações
if Media_Ponderada >= 9.5:
    print ("Aprovado")
else:
    print ("Reprovado")
