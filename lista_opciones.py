#lista de opciones o datos
lista_de_opciones = [
    "Calculadora",
    "Opción 2",
    "Opción 3",
    "Opción 4",
    "Opción 5",
    "Opción 6",
    "Opción 7",
    "Opción 8",
    "Opción 9",
    "Salir"
    
]

#funciones

def cargar_opciones(lista):#función
    imprimirLinea()

    for opcion in lista:
        
        indice = lista.index(opcion)+1
        
        if indice%2 == 0:
           print(f"[{indice}]{opcion}")
        else:
            mensaje = f"[{indice}]{opcion} "
            print(mensaje," " *(15-len(mensaje)),end= "")




def imprimirLinea():
    print("-"*30)
