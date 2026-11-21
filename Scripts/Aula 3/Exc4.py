with open('auth.log') as f:
    texto = f.read()

#COMPARAR TEXTO
minusculas = texto.count("failed")
maiusculas = texto.count("Failed")
print(f"Failed (maiusculas): {maiusculas} | failed (minusculas): {minusculas}")

#CONTAR FAILED SEM MAIUSCULAS
falhadas = texto.lower().count("failed")
print(f"Tentativas falhadas: {falhadas}")

#QUANTOS ATAQUES FEZ O IP
vezes_IP = texto.count("61.177.173.22")
print(f"O IP 61.177.173.22 aparece {vezes_IP} vezes. ")