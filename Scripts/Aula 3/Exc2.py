with open("auth.log") as f:
    texto = f.read()

#CONTAR AS TENTATIVAS FALHADAS
falhadas = texto.count("Failed password")
print(f"Tentativas falhadas: {falhadas}")

#CONTAR OS LOGINS COM SUCESSO
sucesso = texto.count("Accepted password")
print(f"Tentativas sucesso: {sucesso}")

#CONTAR AS LINHAS DO FICHEIRO
linhas = texto.count("\n")
print(f"Total linhas: {linhas}")

#CONTAR AS TENTATIVAS CONTRA O ROOT
contra_root = texto.count("for root")
print(f"Tentativas contra_root: {contra_root}")

#CONTAR AS TENTATIVAS COM UTILIZADORES QUE NAO EXISTEM
invalidos = texto.count("invalid user")
print(f"Utilizadores invalidos: {invalidos}")

#CONTAR AS VEZES QUE APARECE O UTILIZADOR VITOR
vezes_vitor = texto.count("vitor")
print(f"Utilizador vitor aparece: {vezes_vitor}")
