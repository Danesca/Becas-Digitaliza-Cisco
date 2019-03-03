string_list = ["Hola", "esto", "es una", "lista", "de strings"]
integer_list = [1, 2, 3, 4, 5]
multitype_list = ["Hola", 3.141516, 92, "python", 12]

print("Lista de Strings : ", string_list)
print("Lista de Integers : ", integer_list)
print("Lista de Multiples valores : ", multitype_list)

x = string_list[-1]
y = integer_list[-1]
z = multitype_list[-1]

print("Ultimos valores de cada lista : "+x+" "+str(y)+" "+str(z))

##############################

films = {"Clint Eastwood":"Gran Torino","Christopher Nolan":"Origen","Martin Scorsese":"Shutter Island"}
print(films.items())
print(films.keys())
print(films.values())





