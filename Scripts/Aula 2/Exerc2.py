frase = "Diana"
frase_hex = frase.encode().hex()

print(f"Frase original: {frase}")
print(f"Em hexadecimal: {frase_hex}")

frase_original = bytes.fromhex(frase_hex).decode()
print(f"Descodificado: {frase_original}")
