info = ["Nombre", "Apellido", "Telefono", "Ciudad", "Edad"]
infoFilled = []
for x in info:
    infoFilled.append(input("Introduce tu "+x+": "))

print("Gracias",infoFilled[0],infoFilled[1],", tu informacion:",end=' ')
for i in range(2,len(infoFilled)):
    print(info[i]+": "+infoFilled[i],end=', ')
print("ha sido registrada.")

################################# Otra forma de hacerlo ##########################

nombre = input("Introduzca su Nombre: ")
apellidos = input("Introduzca su Apellido: ")
telefono = input("Introduzca su Telefono: ")
ciudad = input("Introduzca su Ciudad: ")
edad = input("Introduzca su Edad: ")

print("Gracias",nombre,apellidos,"su informacion (tlf, ciudad y edad):",telefono,ciudad,edad,"ha quedado registrada")
