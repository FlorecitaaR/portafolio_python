#@sumar funcion que requiere de los parametros
#@ return retorma el resultado de la operación
# a+b

#función siempre tiene return
def sumar(a,b):
    return a+b

# @resultado = 15
#resultado = sumar(10,5) #return 10+5 = 15
#print(resultado)

#multiplicar
def multiplicar(a,b):
    return a * b
resultado = multiplicar (5,5)
print(resultado)

#Restar
def restar(a,b):
    return a - b
resultado = restar(5,1)
print(resultado)

#Dividir
def dividir (a,b):
    return a / b
resultado = dividir(5,2)
print(resultado)

#-------------------
#Programa calculadora
#--------------------
def programa_calculadora():
    print("[1]------------------------")
    print("[1] Multiplicar  [2] Dividir")
    print("[3] Sumar        [4] Restar\n")


    opcion = input("[?]:   ")
    num1 = int(input("[Num1]:   "))
    num2 = int(input("[Num2]:   "))


    if opcion == '1':
        print("[R *]:", multiplicar(num1,num2))
    elif opcion == '2':
        print("[R /]:", dividir(num1,num2))
    elif opcion == '3':
        print("[R +]:", sumar(num1,num2))
    elif opcion == '4':
        print("[R -]:", restar(num1,num2))

    print("-----------------------------------")


    


