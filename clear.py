import os, platform
def limpiar_consola():
    if platform.system()  == "Windows":
        os.system("cls")
    else:
        os.system("clear")
