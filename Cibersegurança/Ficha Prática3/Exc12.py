#variaveis
numero = int(input("Digite um numero inteiro (número negativo encerra): "))

int1 = 0 #0.25
int2 = 0 #26.50
int3 = 0 #51.75
int4 = 0 #76.100

#formula
while numero >= 0:
    if numero >= 0 and numero <= 25:
        int1 = int1 + 1
    elif numero >= 26 and numero <= 50:
        int2 = int2 + 1
    elif numero >= 51 and numero <= 75:
        int3 = int3 + 1
    elif numero >= 76 and numero <= 100:
        int4 = int4 + 1
    numero = int(input("Digite um numero inteiro (número negativo encerra): "))

#resultados
print("Intervalo [0. 25]:", int1)
print("Intervalo [26. 50]:", int2)
print("Intervalo [51. 75]:", int3)
print("Intervalo [76. 100]:", int4)
