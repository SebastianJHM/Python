import funciones_objetivo as fo
import random
import copy


def construccion_inicial_PAES(TP, due_date, ALPHA):
    ## Número de trabajos
    num_trabajos = len(TP)

    solucion = []             ## Secuencia final que será retornada
    solucion_TP = []          ## Tiempos de procesamiento de cada elemento que se guarde en solucion
    
    candidatos = [ i for i in range(1,num_trabajos+1) ] 
    t = 0  ## Parámetro para mdd
    
    ## Pj: parámetro usado en mdd. Suma para cada trabajo el tiempo de procesamiento de cada máquina
    P = [sum(TP[i]) for i in range(num_trabajos)]

    
    for it in range(num_trabajos):
        if( it % 2 == 0):
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
    
            # print("====== Iteración ", it + 1," ======")
            # print("Candidatos: ", candidatos, "Cmax: ", makespan_candidatos, "Min: ", min_mp, "Max: ", max_mp)
    
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
            # print("RCL: ", RCL,"... Menor que: ", indicador)
    
            ## Paso 3: seleccionar aleatoriamente un trabajo del RCL
            pos = random.randint( 1, len(RCL) )   ## Obtener una posicion aleatoria del RCL(funcion aleatorio entre arriba)
            seleccion = RCL[pos-1]                 ## Obtener un trabajo del RCL
        else:
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
        #fi
        solucion.append(seleccion)                 ## Agregrar el trabajo escogido a solución
        candidatos.remove(seleccion)               ## escogido a solucion_TP y remover el elemento de candidatos
        solucion_TP.append(TP[seleccion-1])        ## agregar los tiempos de procesamiento del trabajo escogido a solucion_TP
        t = fo.calcular_makespan_blocking(solucion_TP)
    #rof
    return(solucion)
    
#fed