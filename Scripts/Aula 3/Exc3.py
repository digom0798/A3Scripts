with open('auth.log') as f:
    texto = f.read()

#VERIFICAR AS FAILED PASSWORD
tentativas_falhadas = "Failed password" in texto
print(f"Aparece 'Failed Password'? {tentativas_falhadas}")

#VERIFICAR O IP
ip_google = "8.8.8.8" in texto
print(f"Aparece o IP 8.8.8.8? {ip_google}")

#PEDIR UM IP AO UTILIZADOR
ip_utilizador = input("Escreve um IP para procurar: ")
if ip_utilizador in texto:
    print(f"O IP {ip_utilizador} está no log. ")
else:
    print(f"O IP {ip_utilizador} não está no log. ")

#PEDIR UMA PALAVRA AO UTILIZADOR
palavra_passe = input("Digite uma palavra passe: ")
quantidade = texto.count(palavra_passe)
print(f"A {palavra_passe} aparece {quantidade} vezes. ")
