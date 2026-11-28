falhas = 0

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Failed password" in linha:
            falhas = falhas + 1

print(f"Total de falhas: {falhas}")
