ips_ataques = []

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Failed password" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips_ataques.append(ip)

# 17. Total de ataques
print(f"Total de ataques registados: {len(ips_ataques)}")

# 18. Apenas os IPs diferentes
ips_unicos = set(ips_ataques)
print(f"IPs diferentes: {ips_unicos}")

# 19. Quantos ataques cada IP diferente fez
for ip in ips_unicos:
    print(f"{ip} -> {ips_ataques.count(ip)} ataques")