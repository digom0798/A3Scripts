import getpass
import os
import platform

print(f"Utilizador: {getpass.getuser()}")
print(f"Máquina:{platform.node()}")
print(f"Sistema:{platform.system()} Versão: {platform.release()}")
print(f"Pasta: {os.getcwd()}")

