ips_ataques = []

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Failed password" in linha:
            ip = linha.split("from ")[1].split()[0]
            ips_ataques.append(ip)

for ip in set(ips_ataques):
    if ips_ataques.count(ip) > 3:
        print(f"IP suspeito: {ip} ({ips_ataques.count(ip)} tentativas)")