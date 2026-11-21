import base64
import getpass
import hashlib
import os
import platform

texto = input("Excreve uma frase:")
texto_bytes = texto.encode()

hash_md5 = hashlib.md5(texto_bytes).hexdigest()
hash_sha1 = hashlib.sha1(texto_bytes).hexdigest()
hash_sha256 = hashlib.sha256(texto_bytes).hexdigest()

texto_base64 = base64.b64encode(texto_bytes).decode()
texto_hex = texto_bytes.hex()

utilizador = getpass.getuser()
maquina = platform.node()
sistema = platform.system()
versao = platform.release()
pasta_atual = os.getcwd()

print(f"Utilizador: {utilizador}")
print(f"Maquina: {maquina}")
print(f"Sistema: {sistema}")
print(f"Versao: {versao}")
print(f"Pasta Atual: {pasta_atual}")

print(f"Texto: {texto}")
print(f"Base64: {texto_base64}")
print(f"Hexadecimal: {texto_hex}")

print(f"  MD5: {hash_md5}")
print(f"  SHA-1: {hash_sha1}")
print(f"  SHA256: {hash_sha256}")