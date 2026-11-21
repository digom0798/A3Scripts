# Ler o ficheiro auth.log
with open("auth.log", "r") as f:
    texto = f.read()

# Cálculos
falhadas = texto.count("Failed password")
sucesso = texto.count("Accepted password")
linhas = texto.count("\n")
taxa_falha = (falhadas / linhas) * 100

# Pesquisa interativa de IP
ip_pesquisa = input("Introduz um IP: ")
ataques_pesquisa = texto.count(ip_pesquisa)
print(f"O IP {ip_pesquisa} aparece {ataques_pesquisa} vez(es) no log.")

# Lista dos 4 IPs atacantes
ips_atacantes = \
    ["61.177.173.22",
    "193.168.1.45",
    "222.186.42.7",
    "45.148.10.3",
    "192.168.1.10"]

# 5. Gerar o relatório completo em 'relatorio.txt'
with open("relatorio2.txt", "w") as relatorio2:
    # Cabeçalho
    relatorio2.write("RELATÓRIO COMPLETO DE SEGURANÇA\n")
    relatorio2.write("=" * 30 + "\n")

    # Estatísticas gerais
    relatorio2.write("--- RESUMO GERAL ---\n")
    relatorio2.write(f"Total de linhas analisadas: {linhas}\n")
    relatorio2.write(f"Tentativas falhadas: {falhadas}\n")
    relatorio2.write(f"Logins com sucesso: {sucesso}\n")
    relatorio2.write(f"Taxa de falha: {taxa_falha}\n")

    # Resultado da pesquisa manual
    relatorio2.write("--- PESQUISA DE IP ---\n")
    relatorio2.write(f"IP pesquisado: {ip_pesquisa}, {ataques_pesquisa} ocorrência(s)\n\n")

    # Ataques por cada um dos 4 IPs atacantes
    relatorio2.write("--- ATAQUES POR IP ATACANTE ---\n")
    for ip in ips_atacantes:
        qtd = texto.count(ip)
        relatorio2.write(f"IP {ip}: {qtd} ataque(s)\n")
