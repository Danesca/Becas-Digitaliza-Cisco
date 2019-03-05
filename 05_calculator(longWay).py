def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        value = a/b
        return value
    except:
        print("No es posible dividir entre 0")
        return "Error"


def exponencial(a,b):
    try:
        value = a**b
        return value
    except:
        print("No es posible realizar la exponencial solicitada")
        return "Error"


print("Calculadora: introduzca 2 numeros, por favor")
try:
    a = float(input("a = "))
    b = float(input("b = "))
    dict = {0:"suma", 1:"resta", 2:"multiplicacion", 3:"division", 4:"exponencial"}
    print("¿Que operacion desea realizar?\n",dict)
    operation = int(input())
    result = 0
    if(operation == 0):
        result = suma(a,b)
    elif(operation == 1):
        result = resta(a,b)
    elif(operation == 2):
        result = multiplicacion(a,b)
    elif(operation == 3):
        result = division(a,b)
    elif(operation == 4):
        result = exponencial(a,b)
    else:
        print("Operacion no reconocida")
        result = "Error"

    print("Tu resultado es :", result)
except:
    print("¡Debe introducir un numero!")

