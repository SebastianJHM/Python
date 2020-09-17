def calcular_tardanza_blocking_secuencia( secuencia, TP, due_date ):
    ## mat_t_final[t][m]: tiempo en el que termina el trabajo t en la máquina m
    num_maquinas = len(TP[0])
    num_trabajos = len(TP)
    mat_t_inicial = [[0 for _ in range(num_maquinas)] for _ in range(num_trabajos)] 
    mat_t_final = [[0 for _ in range(num_maquinas)] for _ in range(num_trabajos)] 
    
    ## Obtener matriz según orden de secuencia
    TP_sec = []
    due_date_sec = []
    for x in secuencia:
        TP_sec.append(TP[x-1])
        due_date_sec.append(due_date[x-1])
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
    
    # for x in mat_t:
    #     print(x)
    # #rof

    t_final_trabajos = []
    tardanza_trabajos = []
    for i in range(num_trabajos):
        t_final_trabajos.append(mat_t_final[i][-1])
        if ( due_date_sec[i] < t_final_trabajos[i] ):
            y = t_final_trabajos[i] - due_date_sec[i]
            tardanza_trabajos.append(y)
        else:
            tardanza_trabajos.append(0)
        #fi
    #rof
    # print("Tiempos finales: ", t_final_trabajos)
    # print("Tiempo de entrega: ",due_date_sec)
    # print(tardanza_trabajos, sum(tardanza_trabajos))
    return(sum(tardanza_trabajos), due_date_sec)
#fed


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

    return(mat_t_final[-1][-1], mat_t_inicial, mat_t_final)
#fed