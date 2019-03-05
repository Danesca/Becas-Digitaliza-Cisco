names = []
selected = []
i=0
a_counter=0

while(i<8):
    names.append(input("Introduzca nombre "+str(i+1)+":"))
    if('a' in names[i]):
        a_counter += 1
    if(i == 7 and a_counter < 1):
        print("Debe introducir al menos un nombre que contenga la letra 'a'")
        del(names[-1])
    else:
        i += 1

for singleName in names:
    print(singleName,end=', ')
    if('a' in singleName):
        selected.append(singleName)

print("\nLista selected:", selected)
