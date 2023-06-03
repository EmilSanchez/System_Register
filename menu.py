import os, csv
from clear import limpiar_consola
from registro import registro_user
from registro import registro_tarjeta
import time

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'

def crear_archivos():
    fieldnames_user=["cedula","nombre","direccion","tarjetas"]
    
    with open("datos_usuarios.txt","w",encoding="UTF-8",newline="") as f:
        csv_write = csv.DictWriter(f, fieldnames=fieldnames_user, quotechar='"')
        csv_write.writeheader()
    
    fieldnames_card=["tarjeta","codigo","estado","saldo"]
   
    with open("datos_tarjeta.txt","w",encoding="UTF-8",newline="") as f:
        csv_write = csv.DictWriter(f, fieldnames=fieldnames_card, quotechar='"')
        csv_write.writeheader()
    return

def existencia():
    if os.path.isfile("datos_usuarios.txt") and os.path.isfile("datos_tarjeta.txt"):
        return True
    else:
         return False
       
def menu1():
    valor = existencia()
    if not valor:
        crear_archivos()
    print('=' * 10, " Bienvenido Estimado Cliente ",'=' * 10); print("")
    while True:
        print("Opciones Disponibles...."); print("")
        print("1.   --->  Registrarse                 ")
        print("2.   --->  iniciar seccion     ")
        print("3.   --->  salir")
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
                print("2.   --->  Iniciar seccion        ")
                print("3.   --->  Salir                       ")
                print("")              
                print(RED+"Ingrese una opcion Valida...")
                print(WHITE+"")               
                break
        limpiar_consola()
        if opcion == 1:
            guardar_datos = registro_user()
            print(guardar_datos)
            limpiar_consola()
        elif opcion == 2:
            try: 
                inicar = str(input("Ingrese su numero de documento: "))
                if guardar_datos["cedula"] == inicar: 
                    guardar_tarjeta = registro_tarjeta()
                    try:
                        write_datos(guardar_datos)
                        guardar_datos.pop()
                    except:
                        print("")
                    try:
                        write_tarjeta(guardar_tarjeta)
                        guardar_tarjeta.pop()
                    except:
                        print("") 
                    print(RED+"Sus datos fueron mandados correctamente, saliendo..."); print(WHITE+"")
                    time.sleep(3)
                    limpiar_consola()
                else:
                    print("Su documento no esta registrado, registrese por fabor")
            except:
                print("Su documento no esta registrado, registrese por fabor")
        elif opcion == 3:
            print("¡Hasta pronto!"); print("")
            break
        else: 
            print('=' * 10, " Bienvenido Estimado Cliente ",'=' * 10); print("")
            print(RED+"Esa opcion no existe..."); print(WHITE+"")
            time.sleep(1)
            continue
    return
    
def write_datos(user_datos):
    if len(user_datos) == 4:
        fila = ["cedula","nombre","direccion","tarjetas"]
        with open("datos_usuarios.txt","a",encoding="UTF-8",newline="") as f:
            write = csv.DictWriter(f,fieldnames=fila,quotechar='"')
            write.writerow(user_datos)
    else:
        print()
    return

def write_tarjeta(info_tarjeta):
    fila = ["tarjeta","codigo","estado","saldo"]
    with open("datos_tarjeta.txt","a",encoding="UTF-8",newline="")as f:
        write = csv.DictWriter(f,fieldnames=fila,quotechar='"')
        write.writerow(info_tarjeta)
    return 
