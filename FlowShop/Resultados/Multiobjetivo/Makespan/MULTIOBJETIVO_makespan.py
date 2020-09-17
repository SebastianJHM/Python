import sys
import copy
import random
import fo_makespan as fo
from grasp_tardiness import GRASP_Tardiness
import time

def busqueda_local_GRASP( secuencia, TP, dd, t_max, min_tard ):
    minimo = fo.calcular_makespan_blocking_secuencia(secuencia, TP)
    num_trabajos = len(TP)
    i = 0
    j = 1
    iteraciones = 0
    t_inicial = time.time()
    t_final = time.time() - t_inicial
    while( i < num_trabajos - 1 and t_final <= t_max ):
        
        s = copy.deepcopy(secuencia)
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        # print("\n============== ITERACIÓN ", iteraciones," ===============")
        # print("Secuencia actual: ", secuencia)
        # print(s, fo.calcular_makespan_blocking_secuencia(s,TP))
        # print(i,j)
        
        cmax = fo.calcular_makespan_blocking_secuencia(s,TP)
        tard = fo.calcular_tardanza_blocking_secuencia(s, TP, dd)
        if( cmax < minimo and tard <= min_tard ):
            minimo = cmax
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

# def busqueda_local_GRASP( secuencia, TP, dd, t_max, min_tard ):
#     minimo_make = fo.calcular_makespan_blocking_secuencia(secuencia, TP)
#     minimo_tard = fo.calcular_tardanza_blocking_secuencia(secuencia, TP, dd)
#     num_trabajos = len(TP)
#     i = 0
#     j = 1
#     iteraciones = 0
#     t_inicial = time.time()
#     t_final = time.time() - t_inicial
#     while( i < num_trabajos - 1 and t_final <= t_max ):
        
#         s = copy.deepcopy(secuencia)
#         aux = s[i]
#         s[i] = s[j]
#         s[j] = aux
#         # print("\n============== ITERACIÓN ", iteraciones," ===============")
#         # print("Secuencia actual: ", secuencia)
#         # print(s, fo.calcular_makespan_blocking_secuencia(s,TP))
#         # print(i,j)
        
#         cmax = fo.calcular_makespan_blocking_secuencia(s,TP)
#         tard = fo.calcular_tardanza_blocking_secuencia(s, TP, dd)
#         if( ( cmax < minimo_make and tard <= minimo_tard ) or ( cmax <= minimo_make and tard < minimo_tard ) ):
#             minimo_make = cmax
#             minimo_tard = tard
#             secuencia = s
#             i = 0
#             j = 1
#         else:
#             if( j < num_trabajos - 1 ):
#                 j = j + 1
#             elif( i < num_trabajos - 1 ):
#                 i = i + 1
#                 j = i + 1
#             else:
#                 i = i + 1
#             #fi
#         #fi
#         iteraciones += 1
#         t_final = time.time() - t_inicial
#     #elihw
#     return(secuencia, fo.calcular_makespan_blocking_secuencia(secuencia,TP))
# #fed

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
    ## Paso 1: Determinar conjunto de makespan para cada trabajo candidato = makespan_candidatos, y obtener porcentaje de cada uno
    ## Paso 2: Ordenar conjunto makespan_candidatos de menor a mayor. Con el mismo criterio ordenar el conjunto de candidatos
    ## Paso 3: Determinar el conjuntos de porcentajes de escogencia de cada makespan
    ## Paso 4: Determinar conjunto RCL = {c in candidatos: pocentajes(c) < ALPHA}; Si no queda ninguno escoger el de menor makespan
    ## Paso 5: Seleccionar aleatoriamente un trabajo del RCL
    ## Paso 6: Agregrar el trabajo escogido a solución, agregar los tiempos de procesamiento del trabajo
    ## escogido a solucion_TP y remover el elemento de candidatos
    for _ in range(num_trabajos):
       
        ## Paso1: obtener de los makespan de los candidatos
        makespan_candidatos = []  ## conjunto donde se almacenará el makespan de cada trabajo candidato
        suma_makespan = 0
        for candidato in candidatos:
            s = copy.deepcopy( solucion_TP )     ## Crear una copia de los tiempos de procesamiento de la solucion actual
            s.append(TP[candidato-1])            ## Agregar los tiempos de un posible candidato a la copia creada
            m = fo.calcular_makespan_blocking(s)    ## Calcular el makespan de ese candidato
            makespan_candidatos.append(m)        ## Guardar el makespan
            suma_makespan += m
        #rof
        #print(candidatos, makespan_candidatos)

        ## Paso 2: ordenar conjunto makespan_candidatos
        for i in range(len(makespan_candidatos)):
            for j in range(len(makespan_candidatos)):
                if( makespan_candidatos[j] > makespan_candidatos[i] ):
                    aux = makespan_candidatos[j]
                    makespan_candidatos[j] = makespan_candidatos[i]
                    makespan_candidatos[i] = aux

                    aux = candidatos[j]
                    candidatos[j] = candidatos[i]
                    candidatos[i] = aux
                #fi
            #rof
        #rof
        #print(candidatos, makespan_candidatos)

        ## Paso 3: Determinar el porcentaje para la escogencia
        # porcentajes = [ (i+1)*(1/(len(candidatos))) for i in range(len(candidatos)) ]
        # porcentajes = [ (makespan_candidatos[i])/(suma_makespan) for i in range(len(makespan_candidatos)) ]
        porcentajes = []
        for i in range(len(makespan_candidatos)):
            acum = 0
            for j in range(i+1):
                acum += (makespan_candidatos[j])/(suma_makespan)
            #rof
            porcentajes.append(acum)
        #rof
        #print(porcentajes)

        ## Paso4: Determinar RCL
        RCL = []
        for i in range(len(makespan_candidatos)):
            if ( porcentajes[i] <= ALPHA ):                ## Si el makespan es menor que el ALPHA
                RCL.append(candidatos[i])                  ## guardar el trabajo en RCL
            #fi
        #rof
        ## Si el RCL queda vacío no asignar a nadie
        if ( len(RCL) == 0 ):
            RCL.append(candidatos[0])
        #fi
        #print(RCL)

        ## Paso 5: seleccionar aleatoriamente un trabajo del RCL
        pos = random.randint( 1, len(RCL) )   ## Obtener una posicion aleatoria del RCL(funcion aleatorio entre arriba)
        seleccion = RCL[pos-1]                 ## Obtener un trabajo del RCL
    
        ## Paso 6
        solucion.append(seleccion)                 ## Agregrar el trabajo escogido a solución
        candidatos.remove(seleccion)               ## escogido a solucion_TP y remover el elemento de candidatos
        solucion_TP.append(TP[seleccion-1])        ## agregar los tiempos de procesamiento del trabajo escogido a solucion_TP
    #rof
    return(solucion, fo.calcular_makespan_blocking( solucion_TP))
#fed



def GRASP_Makespan_MO( tp, dd, ALPHA, t_max, ALPHA_tard, t_max_tard ):

    # ## Etapa de construcción de solución
    # secuencia, makespan = construccion_GRASP(tp, ALPHA)
    # print("Secuencia construcción GRASP: ", secuencia, "; Makespan: ", makespan, "; Tardanza: ", fo.calcular_tardanza_blocking_secuencia(secuencia, tp, dd))

    ## Tardanza mínima
    secuencia, min_tard = GRASP_Tardiness(tp, dd, ALPHA_tard, t_max_tard)
    print("Secuencia construcción GRASP: ", secuencia, "; Makespan: ", fo.calcular_makespan_blocking_secuencia(secuencia, tp), "; Tardanza: ", min_tard)
    
    ## Etapa de busqueda local
    secuencia_bl, makespan_bl = busqueda_local_GRASP( secuencia, tp, dd, t_max, min_tard )
    print("Secuencia busqueda local GRASP: ", secuencia_bl, "; Makespan: ", makespan_bl, "; Tardanza: ", fo.calcular_tardanza_blocking_secuencia(secuencia_bl, tp, dd))
    
    return(secuencia, secuencia_bl, min_tard)
#fed