number = int(input("Introduce un numero: "))
if(number < 20):
    print("El numero introducido es menor que 20:",number)
elif(number >= 20 and number <= 39):
    print("El numero introducido se encuentra en el rango 20-39:",number)
elif(number >= 40 and number <= 59):
    print("El numero introducido se encuentra en el rango 40-59:",number)
else:
    print("El numero introducido es mayor que 59:", number)     ### El resto de casos ya estan contemplados con if previos
                                                                ### es decir, solo entrara en el else cuando >= 60