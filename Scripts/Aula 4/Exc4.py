linha = "Failed password for root from 61.177.173.22 port 41200"

ip = linha.split("from")[1].split()[0]
print(ip)

utilizador = linha.split("for")[1].split()[0]
print(utilizador)
