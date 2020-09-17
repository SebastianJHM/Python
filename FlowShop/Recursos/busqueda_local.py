import sys
import copy
import math
import random

def calcular_makespan_blocking_secuencia( secuencia, TP ):
    ## mat_t_final[t][m]: tiempo en el que termina el trabajo t en la máquina m
    num_maquinas = len(TP[0])
    num_trabajos = len(TP)
    mat_t_inicial = [[0 for _ in range(num_maquinas)] for _ in range(num_trabajos)] 
    mat_t_final = [[0 for _ in range(num_maquinas)] for _ in range(num_trabajos)] 
    
    ## Obtener matriz según orden de secuencia
    TP_sec = []
    for x in secuencia:
        TP_sec.append(TP[x-1])
    #rof

    ## Calcular matriz mat_t_final: máquina 1
    for j in range(num_maquinas):
        acum = 0
        for l in range(0,j+1):
            acum += TP_sec[0][l]
        #rof
        mat_t_inicial[0][j] = acum - TP_sec[0][j]
        mat_t_final[0][j] = acum
    #rof

    ## Calcular matriz mat_t_final: para el resto de máquinas
    for t in range(1,num_trabajos):
        for j in range(num_maquinas):
            acum = mat_t_final[t-1][-1]
            for l in range(0,j+1):
                acum += TP_sec[t][l]
            #rof
            mat_t_inicial[t][j] = acum - TP_sec[t][j]
            mat_t_final[t][j] = acum
        #rof
        
        diferencias = []
        minimo = 1000000000000
        for i in range(num_maquinas):
            x = mat_t_inicial[t][i] - mat_t_final[t-1][i]
            diferencias.append(x)
            if ( x < minimo ):
                minimo = x
                pos_menor = i
            #fi
        #rof

        for i in range(num_maquinas):
            mat_t_inicial[t][i] -= diferencias[pos_menor]
            mat_t_final[t][i] -= diferencias[pos_menor]
        #rof
    #rof
    
    ## Matriz de tiempos finales
    mat_t = [[[0,0] for _ in range(num_maquinas)] for _ in range(num_trabajos)]
    for i in range(num_trabajos):
        for j in range(num_maquinas):
            mat_t[i][j][0] = mat_t_inicial[i][j]
            mat_t[i][j][1] = mat_t_final[i][j]
        #rof
    #rof

    return(mat_t_final[-1][-1])
#fed

 
def principal( argv ):
    
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

    secuencia = [5, 2, 4, 1, 3]
    minimo = 100000000000
    for iteraciones in range(5):
        for i in range(len(secuencia)):
            for j in range(i+1,len(secuencia)):
                s = copy.deepcopy(secuencia)
                aux = s[i]
                s[i] = s[j]
                s[j] = aux
                print(s, calcular_makespan_blocking_secuencia(s,TP1)) 
                
                fo = calcular_makespan_blocking_secuencia(s,TP1)
                if( fo < minimo ):
                    minimo = fo
                    secuencia_aux = s
                #fi
            #rof
        #rof
        secuencia = copy.deepcopy(secuencia_aux)
        print(minimo, secuencia_aux)
    #rof
#fed

if __name__ == "__main__":
    principal( sys.argv )
#fi



# def busqueda_local_GRASP( secuencia, TP, num_iteraciones ):
#     minimo = fo.calcular_makespan_blocking_secuencia(secuencia, TP)
#     for iteraciones in range(num_iteraciones):
#         print(iteraciones)
#         for i in range(len(secuencia)):
#             for j in range(i+1,len(secuencia)):
#                 s = copy.deepcopy(secuencia)
#                 aux = s[i]
#                 s[i] = s[j]
#                 s[j] = aux
#                 #print(s, calcular_makespan_blocking_secuencia(s,TP))
#                 print(i,j)
                
#                 f = fo.calcular_makespan_blocking_secuencia(s,TP)
#                 if( f < minimo ):
#                     minimo = f
#                     secuencia_aux = s
#                     break
#                     break
#                 #fi
#             #rof
#         #rof
#         secuencia = copy.deepcopy(secuencia_aux)
#         #print(minimo, secuencia_aux)
#     #rof
#     return(secuencia, fo.calcular_makespan_blocking_secuencia(secuencia,TP))
# #fed

# def busqueda_local_GRASP( secuencia, TP, due_date, num_iteraciones ):
#     minimo = fo.calcular_tardanza_blocking_secuencia( secuencia ,TP, due_date )
#     for iteraciones in range(num_iteraciones):
#         for i in range(len(secuencia)):
#             for j in range(i+1,len(secuencia)):
#                 s = copy.deepcopy(secuencia)
#                 aux = s[i]
#                 s[i] = s[j]
#                 s[j] = aux
#                 #print(s, calcular_makespan_blocking_secuencia(s,TP)) 
                
#                 f = fo.calcular_tardanza_blocking_secuencia( s ,TP, due_date )
#                 if( f < minimo ):
#                     minimo = f
#                     secuencia_aux = s
#                 #fi
#             #rof
#         #rof
#         secuencia = copy.deepcopy(secuencia_aux)
#         #print(minimo, secuencia_aux)
#     #rof
#     return(secuencia, fo.calcular_tardanza_blocking_secuencia( secuencia ,TP, due_date ))
# #fed