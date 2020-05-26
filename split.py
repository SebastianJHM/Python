import sys
from dijkstra import Graph
import Matrices as m

def calcularDistancia(ruta, Distancias):
    d = 0
    for i in range(len(ruta)-1):
        d += Distancias[ruta[i]][ruta[i+1]]
    #rof
    return d
#fed

def obtenerPetalos(GRAFO, RUTAS, sec):
    PETALOS = []
    FO = []
    for i in range(len(sec)-1):
        x = sec[i]
        y = sec[i+1]
        for g in GRAFO:
            if( g[0] == x and g[1] == y ):
                pos = GRAFO.index(g)
                FO.append(g[2])
            #fi
        #rof
        PETALOS.append(RUTAS[pos])
    #rof
    return(PETALOS, FO)
#fed

def SPLIT(Distancias, Demandas, permutacion, capacidad):
    
    NODOS = [i for i in range(len(Distancias))]
    GRAFO = []
    RUTAS = []
    
    for i in range(len(NODOS)):
        for j in range(i+1,len(NODOS)):
            r = [0]
            acum = 0
            for k in range(j,i,-1):
                r.append(permutacion[k-1])
                acum = acum + Demandas[k-1]
            #rof
            r.append(0)
            r.reverse()
            if( acum <= capacidad):
                d = calcularDistancia(r, Distancias)
                arco = (i, j, round(d,2))
                GRAFO.append(arco)
                RUTAS.append(r)
            #fi
        #rof
    #rof
    print("GRAFO:")
    print(GRAFO)
    
    print("RUTA:")
    print(RUTAS)
    
    sec = list(Graph(GRAFO).dijkstra(NODOS[0], NODOS[-1]))
    print("Secuencia: ", sec)
    
    PETALOS, FO = obtenerPetalos(GRAFO, RUTAS, sec)
    print("PETALOS PERMUTACIÓN:")
    print(PETALOS, FO, sum(FO))
    return(PETALOS, FO, sum(FO))
#fed

def principal(argv):
    ## Capacidad del vehículo
    capacidad = 110
    
    ## Matriz de distancias incluyendo el 0
    Distancias = m.Distancias_P1
    
    ## Demandas
    Demandas = [23, 28, 27, 22, 19, 23, 25, 23, 25, 22, 24, 22, 18, 24, 23]

    
    ## Permutación
    mayorista = [4, 12, 24, 13, 16, 28, 11, 32, 33, 40, 23, 26, 44, 10, 22]
    permutacion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


    PETALOS, FO, Fo_T = SPLIT(Distancias, Demandas, permutacion, capacidad)
    for x in PETALOS:
        for y in x:
            if(y != 0):
                x[x.index(y)] = mayorista[y-1] 
            #fi
        #rof
    #rof
    print("PETALOS:")
    print(PETALOS, FO, sum(FO))
    
#fed

if __name__ == "__main__":
    principal(sys.argv)