import platform

sistema = platform.system()
versao = platform.release()
nome_maquina = platform.node()

print(f"Sistema Operativo: {sistema}")
print(f"Versão do Sistema: {versao}")
print(f"Nome da máquina: {nome_maquina}")

