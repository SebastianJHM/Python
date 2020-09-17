import sys
import copy
import random
import fo_makespan as fo
import time

def busqueda_local_GRASP( secuencia, TP, t_max ):
    minimo = fo.calcular_makespan_blocking_secuencia(secuencia, TP)
    num_trabajos = len(TP)
    i = 0
    j = 1
    iteraciones = 0
    t_inicial = time.time()
    t_final = time.time() - t_inicial
    while( i < num_trabajos - 1 and t_final <= t_max ):
        print("\n============== ITERACIÓN ", iteraciones," ===============")
        s = copy.deepcopy(secuencia)
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        print(i,j)
        
        f = fo.calcular_makespan_blocking_secuencia(s,TP)
        print("Secuencia actual: ", secuencia)
        print(s, f)
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
        t_final = time.time() - t_inicial
    #elihw
    return(secuencia, fo.calcular_makespan_blocking_secuencia(secuencia,TP))
#fed

def construccion_GRASP( TP, ALPHA ):

    ## Número de trabajos
    num_trabajos = len(TP)

    solucion = []             ## Secuencia final que será retornada
    solucion_TP = []          ## Tiempos de procesamiento de cada elemento que se guarde en solucion
    
    ## Conjunto de candidatos a ser seleccionados. Si se selecciona un candidato se removerá de candidatos
    ## y se agregará al conjunto solución. Inicialmente en candidatos estarán todos los trabajos i.e. 
    ## candidatos = {1,...,num_trabajos}
    candidatos = [ i for i in range(1,num_trabajos+1) ] 
    
    ## El siguiente ciclo selecciona en cada iteración un posible trabajo para agregarlo a la solución
    ## Paso 1: Determinar conjunto de makespan para cada trabajo candidato, el mínimo de los makespan = min_mp
    ##         y el máximo de los makespan = max_mp
    ## Paso 2: Determinar conjunto RCL = {c in candidatos: makespan(c) < indicador}; indicador = min_mp + ALPHA * ( max_mp - min_mp )
    ## Paso 3: Seleccionar aleatoriamente un trabajo del RCL
    ## Paso 4: Agregrar el trabajo escogido a solución, agregar los tiempos de procesamiento del trabajo
    ## escogido a solucion_TP y remover el elemento de candidatos
    for it in range(num_trabajos):
        makespan_candidatos = []  ## conjunto donde se almacenará el makespan de cada trabajo candidato
        min_mp = 100000000000     ## variable que guardará el mínimo de los makespan
        max_mp = 0                ## variable que guardará el máximo de los makespan
        
        ## Paso1
        for candidato in candidatos:
            s = copy.deepcopy( solucion_TP )     ## Crear una copia de los tiempos de procesamiento de la solucion actual
            s.append(TP[candidato-1])            ## Agregar los tiempos de un posible candidato a la copia creada
            m = fo.calcular_makespan_blocking(s)    ## Calcular el makespan de ese candidato
            makespan_candidatos.append(m)        ## Guardar el makespan
            
            ## Determinar mínimo makespan
            if ( m < min_mp ):
                min_mp = m
            #fi

            ## Determinar máximo makespan
            if ( m > max_mp ):
                max_mp = m
            #fi
        #rof

        print("====== Iteración ", it + 1," ======")
        print("Candidatos: ", candidatos, "Cmax: ", makespan_candidatos, "Min: ", min_mp, "Max: ", max_mp)

        ## Paso2: Determinar RCL
        indicador = min_mp + ALPHA * ( max_mp - min_mp )
        RCL = []
        trabajo = 0
        for m in makespan_candidatos:
            if ( m <= indicador ):                ## Si el makespan es menor que el indicador
                RCL.append(candidatos[trabajo])      ## guardar el trabajo en RCL
            #fi
            trabajo += 1
        #rof
        print("RCL: ", RCL,"... Menor que: ", indicador)

        ## Paso 3: seleccionar aleatoriamente un trabajo del RCL
        pos = random.randint( 1, len(RCL) )   ## Obtener una posicion aleatoria del RCL(funcion aleatorio entre arriba)
        seleccion = RCL[pos-1]                 ## Obtener un trabajo del RCL
        print("Seleccionado: ", seleccion)

        ## Paso 4
        solucion.append(seleccion)                 ## Agregrar el trabajo escogido a solución
        candidatos.remove(seleccion)               ## escogido a solucion_TP y remover el elemento de candidatos
        solucion_TP.append(TP[seleccion-1])        ## agregar los tiempos de procesamiento del trabajo escogido a solucion_TP
        print("Solucion: ", solucion, "Candidatos: ", candidatos)
    #rof
    return(solucion, fo.calcular_makespan_blocking( solucion_TP ))
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

    TP4 = [
        [2, 4, 6, 8, 10],
        [3, 2, 4, 5, 7],
        [4, 3, 1, 4, 5],
        [3, 4, 3, 8, 4],
        [3, 6, 5, 7, 3]
    ]

    ## Etapa de construcción de solución
    ALPHA = 0.5
    secuencia, makespan = construccion_GRASP(TP4, ALPHA)
    print("Secuencia construcción GRASP: ", secuencia, "; Makespan: ", makespan)

    ## Etapa de busqueda local
    num_trabajos = len(TP4)
    num_maquinas = len(TP4[0])
    t_max = 1 * num_trabajos * num_maquinas
    secuencia_bl, makespan_bl = busqueda_local_GRASP( secuencia, TP4, t_max)
    print("Secuencia busqueda local GRASP: ", secuencia_bl, "; Makespan: ", makespan_bl)
#fed

if __name__ == "__main__":
    GRASP( sys.argv )
#fi