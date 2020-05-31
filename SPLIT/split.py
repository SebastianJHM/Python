import sys
from dijkstra import Graph
import Matrices as m

def calcularDistancia(ruta, Distancias, orden):
    t = []
    for y in ruta:
        if(y != 0):
            t.append(orden[y])
        else:
            t.append(0)
        #fi
    #rof

    d = 0
    for i in range(len(t)-1):
        d += Distancias[t[i]][t[i+1]]
    #rof
    return round(d,2)
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

def SPLIT(Distancias, Demandas, permutacion, capacidad, orden):
    
    NODOS = [i for i in range(len(permutacion)+1)]
    GRAFO = []
    RUTAS = []

    for i in range(len(NODOS)):
        for j in range(i+1,len(NODOS)):
            r = [0]
            acum = 0
            for k in range(j,i,-1):
                r.append(permutacion[k-1])
                acum = acum + Demandas[permutacion[k-1]]
            #rof
            r.append(0)
            r.reverse()
            if( acum <= capacidad):
                d = calcularDistancia(r, Distancias, orden)
                arco = (i, j, round(d,2))
                GRAFO.append(arco)
                RUTAS.append(r)
            #fi
        #rof
    #rof
    print("GRAFO:")
    for i in range(len(GRAFO)):
        print(GRAFO[i], ":",RUTAS[i])
    #rof
    
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
    # Distancias = m.Distancias_P1
    # Distancias = m.Distancias_P2
    Distancias = m.Distancias_P3
    
    ## Demandas Yogurt y Queso
    # Demandas = {4: 23, 12: 28, 24: 27, 13: 22, 16: 19, 28: 23, 11: 25, 32: 23, 33: 25, 40: 22, 23: 24, 26: 22, 44: 18, 10: 24, 22: 23}
    # Demandas = {19: 19, 7: 25, 15: 17, 20: 16, 35: 20, 9: 27, 21: 27, 1: 23, 8: 18, 17: 18, 45: 26, 46: 20, 29: 26, 38: 22, 39: 19}
    Demandas = {34: 20, 41: 25, 36: 28, 43: 22, 6: 22, 14: 25, 18: 21, 27: 18, 30: 24, 31: 26, 3: 24, 5: 27, 2: 23, 37: 18, 25: 24, 42: 25}
    
    ## Demandas de Leche
    # Demandas = {4: 21, 12: 21, 24: 19, 13: 15, 16: 20, 28: 22, 11: 22, 32: 13, 33: 22, 40: 20, 23: 16, 26: 16, 44: 18, 10: 16, 22: 20}
    # Demandas = {19: 22, 7: 22, 15: 17, 20: 17, 35: 12, 9: 19, 21: 19, 1: 21, 8: 15, 17: 21, 45: 13, 46: 13, 29: 14, 38: 19, 39: 20}
    # Demandas = {34: 19, 41: 15, 36: 20, 43: 18, 6: 21, 14: 20, 18: 22, 27: 17, 30: 12, 31: 12, 3: 20, 5: 14, 2: 18, 37: 17, 25: 17, 42: 15}
    
    ## Orden en el que parece la referecnia en la matriz
    # orden = {4: 1, 10: 2, 11: 3, 12: 4, 13: 5, 16: 6, 22: 7, 23: 8, 24: 9, 26: 10, 28: 11, 32: 12, 33: 13, 40: 14, 44: 15}
    # orden = {1: 1, 7: 2, 8: 3, 9: 4, 15: 5, 17: 6, 19: 7, 20: 8, 21: 9, 29: 10, 35: 11, 38: 12, 39: 13, 45: 14, 46: 15}
    orden = {2:1, 3:2, 5:3, 6:4, 14:5, 18:6, 25:7, 27:8, 30:9, 31:10, 34:11, 36:12, 37:13, 41:14, 42:15, 43:16}
    
    ## Permutación
    # permutacion = [12, 24, 11, 32, 33, 23]
    # permutacion = [19, 7, 46, 29, 38, 39]
    permutacion = [34, 41, 36, 43, 6, 14, 18, 27, 30, 31, 3, 5, 2, 37, 25, 42]

    PETALOS, FO, Fo_T = SPLIT(Distancias, Demandas, permutacion, capacidad, orden)
    # r = [0, 1, 2, 0]
    # d = calcularDistancia(r, Distancias)
    # print(d)
#fed

if __name__ == "__main__":
    principal(sys.argv)