#Valores da duração das musicas
Segundos_música1 = int(input("Introduza os segundos da música1: "))
Minutos_música1 = int(input("Introduza os minutos da música1: "))

Segundos_música2 = int(input("Introduza os segundos da música2: "))
Minutos_música2 = int(input("Introduza os minutos da música2: "))

Segundos_música3 = int(input("Introduza os segundos da música3: "))
Minutos_música3 = int(input("Introduza os minutos da música3: "))

Segundos_música4 = int(input("Introduza os segundos da música4: "))
Minutos_música4 = int(input("Introduza os minutos da música4: "))

Segundos_música5 = int(input("Introduza os segundos da música5: "))
Minutos_música5 = int(input("Introduza os minutos da música5: "))

#Subtotal dos segundos
Totalsegundos = Segundos_música1 + Segundos_música2 + Segundos_música3 + Segundos_música4 + Segundos_música5

#Subtotal dos minutos
Totalminutos = Minutos_música1 + Minutos_música2 + Minutos_música3 + Minutos_música4 + Minutos_música5

#Converter o tempo para um único valor em segundos
Tempo_total_em_segundos = (Totalminutos * 60) + Totalsegundos

#Calcular horas, minutos e segundos finais
Horas = Tempo_total_em_segundos // 3600
Minutos_Finais = (Tempo_total_em_segundos % 3600) // 60
Segundos_Finais = Tempo_total_em_segundos % 60

#Resultado final
print (f"\nTotal do Albúm: {Horas:02d}:{Minutos_Finais:02d}:{Segundos_Finais:02d}")
