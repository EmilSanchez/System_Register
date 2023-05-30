import os, csv
from clear import limpiar_consola
from registro import registro_user
import time

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'

def existencia():
    if os.path.isfile("datos usuarios.txt"):
        if os.path.isfile("datos tarjeta.txt"):
            return True
        else:
            return False
    else:
        return False

def crear_archivos():
    fieldnames_user=["nombre","cedula","tarjetas"]
    try:
        with open("datos usuarios.txt","w",encoding="UTF-8",newline="") as title:
            csv_write = csv.DictWriter(title, fieldnames=fieldnames_user, quotechar='"')
            csv_write.writeheader()
    except FileNotFoundError:
        return False
    fieldnames_card=["nombre","cedula","tarjeta","codigo","estado","saldo"]
    try:
        with open("datos tarjeta.txt","w",encoding="UTF-8",newline="") as title:
            csv_write = csv.DictWriter(title, fieldnames=fieldnames_card, quotechar='"')
            csv_write.writeheader()
    except FileNotFoundError:
        return False
    return

def menu():
    print('=' * 10, " Bienvenido Estimado Cliente ",'=' * 10); print("")
    while True:
        print("Opciones Disponibles...."); print("")
        print("1.   --->  Registrarse                 ")
        print("2.   --->  Comprar Nueva tarjeta       ")
        print("3.   --->  Recargar tarjeta            ")
        print("4.   --->  Activar/Desactivar (Tarjeta)")
        print("5.   --->  Reporte tarjeta             ")
        print("6.   --->  Salir                       ")
        print("")
        while True:
            try:            
                opcion = int(input("Ingrese la opcion a ejecutar: "))
                break
            except:
                limpiar_consola()
                print('=' * 10, " Bienvenido Estimado Cliente ",'=' * 10); print("")
                print("Opciones Disponibles...."); print("")
                print("1.   --->  Registrarse                 ")
                print("2.   --->  Comprar Nueva tarjeta       ")
                print("3.   --->  Recargar tarjeta            ")
                print("4.   --->  Activar/Desactivar (Tarjeta)")
                print("5.   --->  Reporte tarjeta             ")
                print("6.   --->  Salir                       ")
                print("")              
                print(RED+"Ingrese una opcion Valida...")
                print(WHITE+"")
                time.sleep(1)
                continue
        limpiar_consola()

        if opcion == 1:
            registro_user()
            
        elif opcion == 2:
            pass
            
        elif opcion == 3:
            pass
            
        elif opcion == 4:
            pass
            
        elif opcion == 5:
            pass
            
        elif opcion == 6:
            print("¡Hasta pronto!"); print("")
            exit()
        else: 
            print('=' * 10, " Bienvenido Estimado Cliente ",'=' * 10); print("")
            print(RED+"Esa opcion no existe..."); print(WHITE+"")
            time.sleep(1)
            continue
