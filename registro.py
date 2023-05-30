import random, csv
from clear import limpiar_consola

def registro_user():
    user_datos = {}
    tarjeta_datos = {}
    print("Siga los pasos para registrarse...."); print("")
    nombre=input("Escriba su nombre: ").lower()
    cedula=int(input("Dijite su numero de cedula: "))
    limpiar_consola()
    user_datos["nombre"] = nombre
    tarjeta_datos["cedula"] = cedula
    


