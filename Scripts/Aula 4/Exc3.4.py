palavra = input("Que palavra queres procurar no log? ")

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if palavra in linha:
            print(linha)