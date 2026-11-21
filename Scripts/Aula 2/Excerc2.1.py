import base64
texto = "Scripts é cool"

texto_bytes = texto.encode()
texto_base64 = base64.b64encode(texto_bytes).decode()
texto_hex = texto_bytes.hex()

print(f"Texto original: {texto}")
print(f"Em base 64: {texto_base64}")
print(f"Em hexadecimal: {texto_hex}")

