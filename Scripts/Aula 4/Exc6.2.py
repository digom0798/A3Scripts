ips_ataques = []

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Failed password" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips_ataques.append(ip)

ip_procurado = input("Introduz o IP a pesquisar: ").strip()
print(f"O IP {ip_procurado} fez {ips_ataques.count(ip_procurado)} ataques.")