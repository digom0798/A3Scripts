ips_ataques = []

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Failed password" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips_ataques.append(ip)

with open("relatorio.txt", "w", encoding="utf-8") as relatorio:
    relatorio.write("RELATÓRIO DE ATAQUES POR IP\n")
    relatorio.write("=" * 30 + "\n")
    for ip in set(ips_ataques):
        total = ips_ataques.count(ip)
        relatorio.write(f"{ip}: {total} ataques\n")