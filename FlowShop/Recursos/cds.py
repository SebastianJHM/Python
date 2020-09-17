import sys
import numpy
import copy

def calcular_makespan( secuencia, TP ):
    ## mat_t_final[t][m]: tiempo en el que termina el trabajo t en la máquina m
    num_maquinas = len(TP[0])
    num_trabajos = len(TP)
    mat_t_final = [[0 for _ in range(num_maquinas)] for _ in range(num_trabajos)] 
    
    ## Obtener matriz según orden de secuencia
    TP_sec = []
    for x in secuencia:
        TP_sec.append(TP[x-1])
    #rof
    
    ## Calcular matriz mat_t_final: 3 pasos

    ## Paso1: Llenar los tiempos del trabajo 1
    for j in range(num_maquinas):
        acum = 0
        for l in range(0,j+1):
            acum += TP_sec[0][l]
        #rof
        mat_t_final[0][j] = acum
    #rof
    
    ## Paso2: LLenar los tiempos de todos lo trabajos en la máquina 1
    for i in range(1,num_trabajos):
        acum = 0
        for l in range(i+1):
            acum += TP_sec[l][0]
        #rof
        mat_t_final[i][0] = acum
    #rof
    
    ## Pasao 3: Llenar el resto de la matriz
    for i in range(1,num_trabajos):
        for j in range(1,num_maquinas):
            mat_t_final[i][j] = max(mat_t_final[i-1][j],mat_t_final[i][j-1]) + TP_sec[i][j]
        #rof
    #rof

    # print(numpy.array(mat_t_final))

    return(mat_t_final[-1][-1])
#fed

    

def johnson( TP ):

    ## Secuencia inicial
    num_trabajos = len(TP)

    ## Conjuntos
    trabajos_1 = []
    sec_1 = []
    trabajos_2 = []
    sec_2 = []
    for trabajo in TP:
        if ( trabajo[1] >= trabajo[0] ):
            trabajos_1.append(trabajo)
            sec_1.append( TP.index(trabajo) + 1 )
        else:
            trabajos_2.append(trabajo)
            sec_2.append( TP.index(trabajo) + 1 )
        #fi
    #fi
    # print("Conjunto 1:", trabajos_1, sec_1)
    # print("Conjunto 2:", trabajos_2, sec_2)
    # print("---------------------------------------")

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
    # print("Conjunto ordenado 1: ",trabajos_1, sec_1)

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
    # print("Conjunto ordenado 2: ",trabajos_2, sec_2)
    secuencia = sec_1 + sec_2
    return( secuencia )
#fed


def cds_sets( TP ):
    ## Obtener número de máquinas
    num_maquinas = len(TP[0])
    
    conjuntos = []
    for k in range(1,num_maquinas):
        conjunto = []
        for x in TP:
            aux = []

            ## Primera suma
            acum = 0
            for i in range(0,k):
                acum += x[i]
            #rof
            aux.append(acum)

            ## Segunda suma
            acum = 0
            for i in range(num_maquinas-k,num_maquinas):
                acum += x[i]
            #rof
            aux.append(acum)
            conjunto.append(aux)
        #rod
        conjuntos.append(conjunto)
    #rof
    return conjuntos
#fed

def cds( TP ):
    conjuntos = cds_sets( TP )
    
    # print("----Conjuntos-------")
    # for conjunto in conjuntos:
    #     print("Conjunto", int(conjuntos.index(conjunto))+1,": ", conjunto)
    # #rof
    # print("-------Secuencias--------")

    ## Obtener secuencias
    secuencias = []
    for conjunto in conjuntos:
        secuencia = johnson(conjunto)
        secuencias.append(secuencia)
    #rof
    print(secuencias)
    # ## Imprimir secuencias
    # for secuencia in secuencias:
    #     print("Secuencia", int(secuencias.index(secuencia))+1,": ", secuencia)
    # #rof

    ## Secuencia final
    minimo = 1000000000000
    for secuencia in secuencias:
        makespan = calcular_makespan(secuencia, TP)
        if ( makespan < minimo ):
            minimo = makespan
            pos = int(secuencias.index(secuencia))
        #fi
    #rof

    secuencia_cds = secuencias[pos]
    makespan_cds = minimo
    return( secuencia_cds, makespan_cds)
#fed
    
def principal( argv ):
    print("============= Agoritmo Campbell, Dudek y Smith ============")
    ## Datos iniciales
    # TP = [
    #     [1, 1, 13, 6, 2],
    #     [2, 10, 12, 18, 18],
    #     [3, 17, 9, 13, 4],
    #     [4, 12, 17, 2, 6], 
    #     [5, 11, 3, 5, 16]
    # ]

    TP = [
        [1, 13, 6, 2],
        [10, 12, 18, 18],
        [17, 9, 13, 4],
        [12, 17, 2, 6], 
        [11, 3, 5, 16]
    ]


    ## Obtener secuencia y makespan por algpritmo CDS
    secuencia_cds, makespan_cds = cds( TP )
    print("Secuencia CDS: ", secuencia_cds, "; Makespan: ", makespan_cds)
#fed

if __name__ == "__main__":
    principal( sys.argv )
#fi