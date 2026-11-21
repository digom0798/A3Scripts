#RELATORIO.TXT
with open("auth.log") as f:
    texto = f.read()

#CALCULOS
falhadas = texto.count("Failed password")
sucesso = texto.count("Accepted password")
linhas = texto.count("\n")

taxa_falha = (falhadas / linhas) * 100

#ESCREVER RELATIO NºTENTATIVAS
with open("relatorio.txt", "w") as relatorio:
#CABEÇALHO
    relatorio.write("RELATORIO DE SEGURANCA\n")
    relatorio.write("=" * 30 + "\n")
#ESCREVER RELATORIO NºTENTATIVAS
    relatorio.write(f"Tentativas falhadas: {falhadas}\n")
#LOGINS COM SUCESSO E TOTAL DE LINHAS
    relatorio.write(f"Logins com sucesso: {sucesso}\n")
    relatorio.write(f"Total de linhas: {linhas}\n")
#TAXA DE FALHA
    relatorio.write(f"Taxa de falha: {taxa_falha}\n")
