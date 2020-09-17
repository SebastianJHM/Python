import sys
import copy
import fo_tardiness as fo
import random
from grasp_makespan import GRASP_Makespan
import time

def busqueda_local_GRASP( secuencia, TP, due_date, num_iteraciones  ):
    minimo = fo.calcular_tardanza_blocking_secuencia( secuencia ,TP, due_date )
    num_trabajos = len(TP)
    i = 0
    j = 1
    iteraciones = 0
    while( i < num_trabajos - 1 and iteraciones <= num_iteraciones ):
        # print("\n============== ITERACIÓN ", iteraciones," ===============")
        s = copy.deepcopy(secuencia)
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        #print(s, calcular_makespan_blocking_secuencia(s,TP))
        # print(i,j)
        
        f = fo.calcular_tardanza_blocking_secuencia( s ,TP, due_date )
        # print("Secuencia actual: ", secuencia)
        # print(s, f)
        if( f < minimo ):
            minimo = f
            secuencia = s
            i = 0
            j = 1
        else:
            if( j < num_trabajos - 1 ):
                j = j + 1
            elif( i < num_trabajos - 1 ):
                i = i + 1
                j = i + 1
            else:
                i = i + 1
            #fi
        #fi
        iteraciones += 1
    #elihw
    return(secuencia, fo.calcular_tardanza_blocking_secuencia( secuencia ,TP, due_date ))
#fed

def construccion_GRASP( TP, due_date, ALPHA ):

    ## Número de trabajos
    num_trabajos = len(TP)

    solucion = []             ## Secuencia final que será retornada
    solucion_TP = []          ## Tiempos de procesamiento de cada elemento que se guarde en solucion
    
    ## Conjunto de candidatos a ser seleccionados. Si se selecciona un candidato se removerá de candidatos
    ## y se agregará al conjunto solución. Inicialmente en candidatos estarán todos los trabajos i.e. 
    ## candidatos = {1,...,num_trabajos}
    candidatos = [ i for i in range(1,num_trabajos+1) ] 
    t = 0  ## Parámetro para mdd

    ## Pj: parámetro usado en mdd. Suma para cada trabajo el tiempo de procesamiento de cada máquina
    P = []
    for i in range(num_trabajos):
        P.append(sum(TP[i]))
    #rof
    # print("P: ", P, "Due date: ", due_date)
    
    ## El siguiente ciclo selecciona en cada iteración un posible trabajo para agregarlo a la solución
    ## Paso 1: Determinar conjunto de mdd para cada trabajo candidato, el mínimo de los mdd = min_mdd
    ##         y el máximo de los mdd = max_mdd
    ## Paso 2: Determinar conjunto RCL = {c in candidatos: makespan(c) < indicador}; indicador = min_mp + ALPHA * ( max_mp - min_mp )
    ## Paso 3: Seleccionar aleatoriamente un trabajo del RCL
    ## Paso 4: Agregrar el trabajo escogido a solución, agregar los tiempos de procesamiento del trabajo
    ## escogido a solucion_TP y remover el elemento de candidatos
    for it in range(num_trabajos):
        MMD = []  ## conjunto donde se almacenará el MMD de cada trabajo candidato
        min_mdd = 100000000000     ## variable que guardará el mínimo de los makespan
        max_mdd = 0                ## variable que guardará el máximo de los makespan
        
        ## Paso1
        for candidato in candidatos:
            y = max( P[candidato-1], due_date[candidato-1] - t )
            MMD.append(y)
            ## Determinar mínimo makespan
            if ( y < min_mdd ):
                min_mdd = y
            #fi
            ## Determinar máximo makespan
            if ( y > max_mdd ):
                max_mdd = y
            #fi
        #rof
        
        # print("====== Iteración ", it + 1," ======")
        # print("Candidatos: ", candidatos, "MMD: ", MMD, "Min: ", min_mdd, "Max: ", max_mdd)

        ## Paso2: Determinar RCL
        indicador = min_mdd + ALPHA * ( max_mdd - min_mdd )
        RCL = []
        trabajo = 0
        for m in MMD:
            if ( m <= indicador ):                ## Si el makespan es menor que el indicador
                RCL.append(candidatos[trabajo])        ## guardar el trabajo en RCL
            #fi
            trabajo += 1
        #rof
        # print("RCL: ", RCL,"... Menor que: ", indicador)

        ## Paso 3: seleccionar aleatoriamente un trabajo del RCL
        pos = random.randint( 1, len(RCL) )   ## Obtener una posicion aleatoria del RCL(funcion aleatorio entre arriba)
        seleccion = RCL[pos-1]                 ## Obtener un trabajo del RCL
        # print("Seleccionado: ", seleccion)

        ## Paso 4
        solucion.append(seleccion)                 ## Agregrar el trabajo escogido a solución
        candidatos.remove(seleccion)               ## escogido a solucion_TP y remover el elemento de candidatos
        solucion_TP.append(TP[seleccion-1])        ## agregar los tiempos de procesamiento del trabajo escogido a solucion_TP
        t = fo.calcular_makespan_blocking(solucion_TP)
        # print("Solucion: ", solucion, "Candidatos: ", candidatos)
        # print("t: ", t)
    #rof
    return(solucion, fo.calcular_tardanza_blocking_secuencia( solucion ,TP, due_date ))
#fed


def GRASP( argv ):
    ## TP[t][m]: tiempo de procesamiento del trabajo t en la máquina m.
    TP1 = [
        [45, 13, 26, 24],
        [25, 76, 14, 73],
        [56, 76, 20, 24],
        [39, 51, 7, 6],
        [61, 23, 43, 85],
    ]
    
    TP2 = [
        [3, 3, 2],
        [2, 1, 3],
        [4, 1, 3],
    ]

    TP3 = [
        [1, 13, 6, 2],
        [10, 12, 18, 18],
        [17, 9, 13, 4],
        [12, 17, 2, 6],
        [11, 3, 5, 16]
    ]
    due_date3 = [20, 75, 45, 34, 41]

    ## Etapa de construcción de solución
    ALPHA = 0.6
    secuencia, tardanza = construccion_GRASP(TP3, due_date3, ALPHA)
    print("Secuencia construcción GRASP: ", secuencia, "; Tardanza: ", tardanza, "; Makespan: ", fo.calcular_makespan_blocking_secuencia(secuencia, TP3))

    ## Tardanza mínima
    ALPHA_tard = 0.5
    num_iteraciones_tard = 1
    min_makespan = GRASP_Makespan(TP3, ALPHA_tard, num_iteraciones_tard) 
    print("Makespan mínimo: ", min_makespan)
    
    ## Etapa de busqueda local
    num_iteraciones = 30
    secuencia_bl, makespan_bl = busqueda_local_GRASP( secuencia, TP3, due_date3, num_iteraciones, min_makespan )
    print("Secuencia busqueda local GRASP: ", secuencia_bl, "; Tardanza: ", makespan_bl, "; Makespan: ", fo.calcular_makespan_blocking_secuencia(secuencia_bl, TP3))
#fed

if __name__ == "__main__":
    start_time = time.time()
    GRASP( sys.argv )
    print("t: ", time.time() - start_time)
#fi