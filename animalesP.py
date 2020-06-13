import json

JSONDATA = None
with open ('animales.json') as f:
    JSONDATA = json.load(f)
    
if not JSONDATA:
    exit

ave = 0
reptil = 0
mamifero = 0
n=0
m=0
encontrado=0

animal = input("¿Cuál es el nombre del animal?: \n")

for e in JSONDATA['Defecto']:
    if animal == (JSONDATA['Defecto'][n]["Nombre"]):
        print ("\n"+"Ave: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Ave"]))
        print ("Reptil: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Reptil"]))
        print ("Mamifero: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Mamifero"]))
        print ("\n"+"Tu animal es: "+animal)
        encontrado=1
        n = n+1
	
if encontrado == 1:
    exit()
	
for i in JSONDATA['Nodos']:
	print("Tiene | puede | es :")
	print (JSONDATA['Nodos'][m][1]) 
	s = input("")
	if s == "s":
		ave = (JSONDATA['Nodos'][m][2]["Ave"]) + ave 
		reptil = (JSONDATA['Nodos'][m][2]["Reptil"]) + reptil
		mamifero = (JSONDATA['Nodos'][m][2]["Mamifero"]) + mamifero
	m=1+m
	
print("\n"+"Ave: " + str(ave))
print("Reptil: " + str(reptil))
print("Mamifero: " + str(mamifero))

total=ave+reptil+mamifero
print ("Total: "+str(total))
pave=(ave/total)
preptil=(reptil/total)
pmamifero=(mamifero/total)

print("\n"+"El nombre del animal es: " + animal)
print("\n"+"La probabilidad de que sea un ave es: " + str(pave))
print("\n"+"La probabilidad de que sea un reptil es: " + str(preptil))
print("\n"+"La probabilidad de que sea un mamífero es: " + str(pmamifero))