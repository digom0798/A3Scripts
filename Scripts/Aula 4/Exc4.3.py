with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Accepted password" in linha:
            utilizador = linha.split("for ")[1].split()[0]
            print(utilizador)