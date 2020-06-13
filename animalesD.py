"""
		Estrategia 1:
		Preguntar todo y sumar los puntajes.
		Finalizar colocando los puntajes
		y tomando la determinanción si es
		ave, reptil o mamífero.
"""
import json

JSONDATA = None
with open ('animales.json') as f:
    JSONDATA = json.load(f)
    
if not JSONDATA:
	exit()
	
suma = [0,0,0]
n = 0
encontrado = 0
pregunta = False
print("¿Cuál es el nombre del animal?: ")
A = input("")
for e in JSONDATA['Defecto']:
    if A == (JSONDATA['Defecto'][n]["Nombre"]):
        print ("\n"+"Ave: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Ave"]))
        print ("Reptil: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Reptil"]))
        print ("Mamifero: " +str(JSONDATA['Defecto'][n]["Puntaje"]["Mamifero"]))
        print ("\n"+"Tu animal es: "+A)
        encontrado = 1
    n = n + 1
if encontrado == 1:
    exit()
    
while not pregunta:
    for pregunta in JSONDATA['Nodos']:
        print("Tiene | puede | es :")
        print(pregunta[1])
        R = input("")
        if R == "s" :
            suma[0] = suma[0]+pregunta[2]['Ave']
            suma[1] = suma[1]+pregunta[2]['Reptil']
            suma[2] = suma[2]+pregunta[2]['Mamifero']
print(" ")
print(suma[0],"Ave")
print(suma[1],"Reptil")
print(suma[2],"Mamifero")