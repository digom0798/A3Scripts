total = 0

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        total = total + 1

print(f"Total de linhas {total}")
