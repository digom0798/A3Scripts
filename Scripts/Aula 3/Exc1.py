#Abrir o ficheiro
with open("auth.log") as f:
    texto = f.read()

#Imprimir o conteudo
print("1. CONTEUDO COMPLETO")
print(texto)

#Mostra quantos caracteres tem o ficheiro
print("2. TOTAL DE CARACTERES")
print(f"O ficheiro tem {len(texto)} caracteres")

#Mostra o log em maiusculas
print("3. LOG EM MAIUSCULAS")
print(texto.upper())

#Mostra os primeiros 200 caracteres
print("4. PRIMEIROS 200 CARACTERES")
print(texto[:200])
