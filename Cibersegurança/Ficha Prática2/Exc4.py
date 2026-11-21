#Lugar na corrida
Lugar_corrida = int(input("Introduza o seu lugar na corrida: "))

#Pontos na corrida
if Lugar_corrida == 1:
    Pontos = 10
if Lugar_corrida == 2:
    Pontos = 8
if Lugar_corrida == 3:
    Pontos = 6
if Lugar_corrida == 4:
    Pontos = 5
if Lugar_corrida == 5:
    Pontos = 4
if Lugar_corrida == 6:
    Pontos = 3
if Lugar_corrida == 7:
    Pontos = 2
if Lugar_corrida == 8:
    Pontos = 1
if Lugar_corrida > 8 or Lugar_corrida < 1:
    Pontos = 0

#Resultado
if Pontos > 0:
    print(f"O piloto terminou em {Lugar_corrida}º lugar e ganhou {Pontos} ponto(s).")
else:
    print(f"O piloto terminou em {Lugar_corrida}º lugar e não ganhou ponto(s).")