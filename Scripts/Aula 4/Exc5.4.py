utilizadores_sucesso = []

with open("auth.log", "r", encoding="utf-8") as ficheiro:
    for linha in ficheiro:
        if "Accepted password" in linha:
            user = linha.split("for ")[1].split()[0]
            utilizadores_sucesso.append(user)

print(f"Todos os logins com sucesso: {utilizadores_sucesso}")
print(f"Utilizadores diferentes: {set(utilizadores_sucesso)}")