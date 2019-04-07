def calculadora(operacion, a, b):
    try:
        if(operacion != 3 and b == 0):
            dict = {0:a+b, 1:a-b, 2:a*b, 3:0, 4:a**b}
        else:
            dict = {0:a+b, 1:a-b, 2:a*b, 3:a/b, 4:a**b}
        print("Su resultado es: ", dict[operacion])
    except:
        if(operacion > 4):
            print("La operacion solicitada no existe")
        else:
            print("La operacion solicitada no puede realizarse")

try:
    a = float(input("Introduzca primer numero: "))
    b = float(input("Introduzca segundo numero: "))
    op = int(input("¿Que operacion desea realizar? 0 - suma, 1 - resta, 2 - multiplicacion, 3 - division, 4 - exponencial: "))
    calculadora(op,a,b)
except:
    print("¡Debe introducir un numero!")
