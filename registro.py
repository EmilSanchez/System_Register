import random, csv
from clear import limpiar_consola
import random

def registro_user():
    user_datos = {}
    print("Siga los pasos para registrarse...."); print("")
    nombre=input("Escriba su nombre: ")
    cedula=input("Dijite su numero de cedula: ")
    direccion=input("Ingrese su dirección: ")
    tarjetas = input("Ingrese la cantidad de tarjetas que tiene: ")
    user_datos["cedula"] = cedula
    user_datos["nombre"] = nombre
    user_datos["direccion"] = direccion
    user_datos["tarjetas"] = tarjetas
    print(len(user_datos))
    return user_datos

def registro_tarjeta():
    info_tarjeta = {}
    print("Compra de Tarjeta")
    codigo = "0123456789"
    logitud = 5
    codigo = random.sample(codigo,logitud)
    codigo= "".join(codigo)
    print(f"El codigo de su tarjeta es -> {codigo}")
    estado = "activa"
    tarjeta = input("Ingrese la cantidad de tarjetas que desea comprar: ")
    info_tarjeta["tarjeta"] = tarjeta
    info_tarjeta["codigo"] = codigo
    info_tarjeta["estado"] = estado
    saldo = int(input("Ingrese el valor de la recarga -> "))
    saldo = str(saldo)
    info_tarjeta["saldo"] = saldo
    print(info_tarjeta)

    return info_tarjeta
    


    


