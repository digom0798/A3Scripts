#Horários
Horas = int(input("Introduza as horas (0-23)? "))
Minutos = int(input("Introduza as minutos (0-59)? "))

#Resultado
if Horas >= 12:
    print(f"{Horas}:{Minutos} PM")
else:
    print(f" {Horas}:{Minutos} AM")