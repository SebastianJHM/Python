import sys
import copy 

def johnson( data ):

    ## Secuencia inicial
    num_trabajos = len(data)

    ## Conjuntos
    trabajos_1 = []
    sec_1 = []
    trabajos_2 = []
    sec_2 = []
    for trabajo in data:
        if ( trabajo[1] >= trabajo[0] ):
            trabajos_1.append(trabajo)
            sec_1.append( data.index(trabajo) + 1 )
        else:
            trabajos_2.append(trabajo)
            sec_2.append( data.index(trabajo) + 1 )
        #fi
    #fi
    print("Conjunto 1:", trabajos_1, sec_1)
    print("Conjunto 2:", trabajos_2, sec_2)
    print("---------------------------------------")

    ## Algoritmo de ordenamiento Conjunto 1 ( menor a mayor en máquina 1)
    for i in range(len(trabajos_1)):
        for j in range(i+1,len(trabajos_1)):
            if( trabajos_1[i][0] >= trabajos_1[j][0] ):
                aux = trabajos_1[i]
                trabajos_1[i] = trabajos_1[j]
                trabajos_1[j] = aux

                s = sec_1[i]
                sec_1[i] = sec_1[j]
                sec_1[j] = s
            #fi
        #rof
    #rof
    print("Conjunto ordenado 1: ",trabajos_1, sec_1)

    ## Algoritmo de ordenamiento Conjunto 2 ( mayor a menor en máquina 2)
    for i in range(len(trabajos_2)):
        for j in range(i+1,len(trabajos_2)):
            if( trabajos_2[i][1] <= trabajos_2[j][1] ):
                aux = trabajos_2[i]
                trabajos_2[i] = trabajos_2[j]
                trabajos_2[j] = aux

                s = sec_2[i]
                sec_2[i] = sec_2[j]
                sec_2[j] = s
            #fi
        #rof
    #rof
    print("Conjunto ordenado 2: ",trabajos_2, sec_2)
    secuencia = sec_1 + sec_2
    return( secuencia )
#fed

def principal( argv ):

    ## Datos iniciales para algoritmo de Johnson
    ## Trabajo-Tiempo M1-Tiempo M2
    # data = [
    #     [1, 6, 3],
    #     [2, 2, 9],
    #     [3, 4, 3],
    #     [4, 1, 8],
    #     [5, 7, 1],
    #     [6, 4, 5],
    #     [7, 7, 6]
    # ]
    data = [
        [6, 3],
        [2, 9],
        [4, 3],
        [1, 8],
        [7, 1],
        [4, 5],
        [7, 6]
    ]
    ## Obtener secuencia final
    secuencia = johnson(data)
    print("Secuencia Final Johnson: ", secuencia)
#fed

if __name__ == "__main__":
    principal( sys.argv )
#fi