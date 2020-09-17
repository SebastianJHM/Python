import sys
import copy

def johnson( data ):
    trabajos_1 = []
    trabajos_2 = []
    for trabajo in data:
        if ( trabajo[2] >= trabajo[1] ):
            trabajos_1.append(trabajo)
        else:
            trabajos_2.append(trabajo)
        #fi
    #fi
    # print("Conjunto 1:", trabajos_1)
    # print("Conjunto 2:", trabajos_2)
    # print("---------------------------------------")

    ## Algoritmo de ordenamiento Conjunto 1 ( menor a mayor en máquina 1)
    for i in range(len(trabajos_1)):
        for j in range(i+1,len(trabajos_1)):
            if( trabajos_1[i][1] > trabajos_1[j][1] ):
                aux = trabajos_1[i]
                trabajos_1[i] = trabajos_1[j]
                trabajos_1[j] = aux
            #fi
        #rof
    #rof
    # print("Conjunto ordenado 1: ",trabajos_1)

    ## Algoritmo de ordenamiento Conjunto 2 ( mayor a menor en máquina 2)
    for i in range(len(trabajos_2)):
        for j in range(i+1,len(trabajos_2)):
            if( trabajos_2[i][2] < trabajos_2[j][2] ):
                aux = trabajos_2[i]
                trabajos_2[i] = trabajos_2[j]
                trabajos_2[j] = aux
            #fi
        #rof
    #rof
    # print("Conjunto ordenado 2: ",trabajos_2)

    ## Guardar secuencia final
    secuencia = []
    for x in trabajos_1:
        secuencia.append(x[0])
    #rof
    for x in trabajos_2:
        secuencia.append(x[0])
    #rof
    return(secuencia)
#fed


def cds( data ):

    data1 = []
    ## Conjunto 1
    for x in data:
        aux = []
        aux.append(x[0])
        aux.append(x[1])
        aux.append(x[4])
        data1.append(aux)
    #rof
    print("Data 1:", data1)

    ## Conjunto 2
    data2 = []
    for x in data:
        aux = []
        aux.append(x[0])
        aux.append(x[1]+x[2])
        aux.append(x[3]+x[4])
        data2.append(aux)
    #rof
    print("Data 2: ", data2)

    ## Conjunto 3
    data3 = []
    for x in data:
        aux = []
        aux.append(x[0])
        aux.append(x[1]+x[2]+x[3])
        aux.append(x[2]+x[3]+x[4])
        data3.append(aux)
    #rof
    print("Data 3: ", data3)
    return(data1, data2, data3)
#fed

def principal( argv ):

    ## Datos iniciales
    data = [
        [1, 1, 13, 6, 2],
        [2, 10, 12, 18, 18],
        [3, 17, 9, 13, 4],
        [4, 12, 17, 2, 6],
        [5, 11, 3, 5, 16]
    ]

    conjuntos = cds( data )
    
    secuencias = []
    for conjunto in conjuntos:
        secuencia = johnson(conjunto)
        print("Secuencia", int(conjuntos.index(conjunto))+1,": ", secuencia)
        secuencias.append(secuencia)
    #rof
#fed

if __name__ == "__main__":
    principal( sys.argv )
#fi