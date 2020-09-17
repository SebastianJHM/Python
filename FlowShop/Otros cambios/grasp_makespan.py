import sys
import copy
import random
import fo_makespan as fo
from leer_instancias_pruebas import read_data_XLSX

def busqueda_local_GRASP( secuencia, TP, num_iteraciones ):
    minimo = fo.calcular_makespan_blocking_secuencia(secuencia, TP)
    for iteraciones in range(num_iteraciones):
        s = copy.deepcopy(secuencia)
        
        ## Realizar cambios 
        n = 4
        for _ in range(n):
            x = random.randint(0,len(s)-1)
            y = random.randint(0,len(s)-1)
            while( y == x ):
                y = random.randint(0,len(s)-1)
            #elihw
            aux = s[x]
            s[x] = s[y]
            s[y] = aux
        #rof
        #print(s, calcular_makespan_blocking_secuencia(s,TP)) 
        
        f = fo.calcular_makespan_blocking_secuencia(s,TP)
        if( f < minimo ):
            minimo = f
            secuencia = s
            # print(s)
        #fi
    #rof
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
        # print("Seleccionado: ", seleccion)

        ## Paso 4
        solucion.append(seleccion)                 ## Agregrar el trabajo escogido a solución
        candidatos.remove(seleccion)               ## escogido a solucion_TP y remover el elemento de candidatos
        solucion_TP.append(TP[seleccion-1])        ## agregar los tiempos de procesamiento del trabajo escogido a solucion_TP
        # print("Solucion: ", solucion, "Candidatos: ", candidatos)
    #rof
    return(solucion, fo.calcular_makespan_blocking( solucion_TP ))
#fed
 
def GRASP( argv ):
    INSTANCIAS = read_data_XLSX()
    
    for inst in INSTANCIAS:
        print("------------------------------------------------")
        ## Parámetros de la instancia
        tp = inst.tiempos_procesamiento
        dd = inst.due_dates
        
        ## Etapa de construcción de solución
        ALPHA = 0.5
        secuencia, makespan = construccion_GRASP(tp, ALPHA)
        print("Secuencia construcción GRASP: ", secuencia, "; Makespan: ", makespan)
    
        ## Etapa de busqueda local
        num_iteraciones = 10000
        secuencia_bl, makespan_bl = busqueda_local_GRASP( secuencia, tp, num_iteraciones )
        print("Secuencia busqueda local GRASP: ", secuencia_bl, "; Makespan: ", makespan_bl)
#fed

if __name__ == "__main__":
    GRASP( sys.argv )
#fi