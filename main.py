#modulos
import os
#modulos importar funciones
from lista_opciones import cargar_opciones
from calculadora import programa_calculadora

#limpiar terminal inicio del programa
os.system("cls")

cargar_opciones()
#creando una variable que muestre la obsion que el usuario muestre

try: #SI NO HAY ERRORES
    respuesta = input("[?]")

    if respuesta == "1":
        programa_calculadora()

except:#SI HAY ERROR
    print("valor nulo")