"""
    Programa reinas.
    Hernández Ángeles María Guadalupe Catalina  15590697
    Vega Reséndiz Ricardo                       15590740
    
"""

tablero =[[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
posAct=[]
llave = 0
posiciones = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

def reinas(nreinas, tablero, llave,posiciones):
    backup = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    cont = 0
    print("Reinas: "+str(nreinas))
    if nreinas == 1:
        return solucion(tablero)
    else: 
        for t in range(len(tablero)):
            for r in range(len(tablero[t])):
                if cont == 0:
                    if posiciones[t][r] != 3:
                        if(tablero[t][r] == 0):
                            if nreinas == 4:
                                posiciones[t][r] = 3
                            tablero[t][r] = 1
                            cont = cont + 1
                            posAct.append([t,r])
        tablero = vertHorz(tablero,posAct)
        posAct.pop(0)
        for t in tablero:
            if 0 in t:
                llave = 0
            else:
                llave = 1
        if llave == 1:
            print(llave)
            for t in backup:
                print(t)
            nreinas=4
            llave=0
            return reinas(nreinas,backup,llave,posiciones)
        if llave == 0:
            print(llave)
            nreinas=nreinas-1
            return reinas(nreinas,tablero,llave,posiciones)

def vertHorz(tablero,posAct):
    print("============")
    a = posAct[0][0]
    b = posAct[0][1]
    r = range(len(tablero))
    bb = b
    aa = a
    print(posAct)   
    for t in range(len(tablero)):
        for r in range(len(tablero[t])):
            tablero[a][r] = 2
            tablero[t][b] = 2
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb-1
        aa = aa -1
        if (bb >= 0)and(aa >=0):
            print("- -")
            tablero[aa][bb] = 2
    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        aa = aa +1
        bb = bb +1
        if (aa <= r)and(bb <= r):
            print("+ +")
            tablero[aa][bb] = 2
    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb+1
        aa = aa -1
        if (bb < r)and(aa >=0):
            print("+ -")
            tablero[aa][bb] = 2
    bb = b
    aa = a
    imp(tablero)
    for t in range(len(tablero)):
        bb = bb-1
        aa = aa + 1
        if (bb >= 0)and(aa <r):
            print("- +")
            tablero[aa][bb] = 2
    tablero[a][b]=1
    imp(tablero)
    print("============")
    return tablero
    
def solucion(tablero):
    for t in range(len(tablero)):
        for r in range(len(tablero[t])):
            if (tablero[t][r]) == 0:
                tablero[t][r] = 1
    print("\n"+"======= Solución ======="+"\n")
    for t in tablero:
        print(t)

def imp(tablero):
    print("============")
    for t in tablero:
        print(t)

reinas(4,tablero,0,posiciones)