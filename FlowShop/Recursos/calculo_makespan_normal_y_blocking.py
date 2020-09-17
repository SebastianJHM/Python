import sys
import numpy

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

    #print(numpy.array(mat_t_final))
    ## Matriz de tiempos finales
    mat_t = [[[0,0] for _ in range(num_maquinas)] for _ in range(num_trabajos)]
    for i in range(num_trabajos):
        for j in range(num_maquinas):
            mat_t[i][j][0] = mat_t_final[i][j] - TP_sec[i][j]
            mat_t[i][j][1] = mat_t_final[i][j]
        #rof
    #rof
    
    for x in mat_t:
        print(x)
    #rof
    return(mat_t_final[-1][-1])
#fed
    
def calcular_makespan_blocking( secuencia, TP ):
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
    
    for x in mat_t:
        print(x)
    #rof
    return(mat_t_final[-1][-1])
#fed

def principal( argv ):
    
    ## TP[t][m]: tiempo de procesamiento del trabajo t en la máquina m.
    TP1 = [
        [1, 13, 6, 2],
        [10, 12, 18, 18],
        [17, 9, 13, 4],
        [12, 17, 2, 6],
        [11, 3, 5, 16]
    ]
    #secuencia = [2, 3, 4, 5, 1]
    secuencia = [1, 5, 2, 3, 4]

    ## TP[t][m]: tiempo de procesamiento del trabajo t en la máquina m.
    TP2 = [
        [3, 3, 2],
        [2, 1, 3],
        [4, 1, 3],
    ]
    #secuencia = [1, 2, 3]

    TP3 = [
        [45, 13, 26, 24],
        [25, 76, 14, 73],
        [56, 76, 20, 24],
        [39, 51, 7, 6],
        [61, 23, 43, 85],
    ]
    #secuencia = [1, 4, 3, 5, 2]

    makespan = calcular_makespan( secuencia, TP1 )
    print("Makespan normal: ", makespan )
    print("-------------------")
    makespan = calcular_makespan_blocking( secuencia, TP1 )
    print("Makespan con blocking: ", makespan )
#fed

if __name__ == "__main__":
    principal( sys.argv )
#fi