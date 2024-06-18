def grafica_frecuencias(lista):
    # Iterar sobre cada elemento de la lista
    for p in lista:
        # Mostrar el nombre del producto
        print(p["producto"], " ", end="")
        # Iterar según la frecuencia del producto
        for n in range(p["f"]):
            # Mostrar un '0' por cada unidad de frecuencia
            print("0", end="")
        # Espacio Vacio
        print("")