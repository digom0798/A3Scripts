with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "for root" in linha:
            print(linha)
