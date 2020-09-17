import sys
import copy
import random
import fo_makespan as fo

## Busqueda local
## Paso 1: Realizar de a parejas entre todos los posibles elementos de la secuencia
## Paso 2: Evaluar función objetivo del intercambio y seleccionar la mejor
## Paso 3: actualizar secuencia
def busqueda_local_GRASP( secuencia, TP, num_iteraciones ):
    minimo = 100000000000
    for iteraciones in range(num_iteraciones):
        for i in range(len(secuencia)):
            for j in range(i+1,len(secuencia)):
                ## Paso 1
                s = copy.deepcopy(secuencia)
                aux = s[i]
                s[i] = s[j]
                s[j] = aux
                #print(s, calcular_makespan_blocking_secuencia(s,TP)) 
                
                ## Paso 2
                f = fo.calcular_makespan_blocking_secuencia(s,TP)
                if( f < minimo ):
                    minimo = f
                    secuencia_aux = s
                #fi
            #rof
        #rof
        ## Paso 3
        secuencia = copy.deepcopy(secuencia_aux)
        #print(minimo, secuencia_aux)
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
        print(candidatos, makespan_candidatos)

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
        print(porcentajes)

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
    secuencia, makespan = construccion_GRASP(TP3, ALPHA)
    print("Secuencia construcción GRASP: ", secuencia, "; Makespan: ", makespan, "; Tardanza: ", fo.calcular_tardanza_blocking_secuencia(secuencia, TP3, due_date3))

    ## Etapa de busqueda local
    num_iteraciones = 30
    secuencia_bl, makespan_bl = busqueda_local_GRASP( secuencia, TP3, num_iteraciones )
    print("Secuencia busqueda local GRASP: ", secuencia_bl, "; Makespan: ", makespan_bl, "; Tardanza: ", fo.calcular_tardanza_blocking_secuencia(secuencia_bl, TP3, due_date3))
#fed

if __name__ == "__main__":
    GRASP( sys.argv )
#fi