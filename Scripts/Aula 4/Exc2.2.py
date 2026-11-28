numero = 1

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        print(f"{numero}:{linha.strip()}")
        numero = numero + 1
