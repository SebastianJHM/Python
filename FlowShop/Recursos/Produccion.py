## PROGRAMACIÓN FLOWSHOP DE PRODUCCIÓN

## El siguiente caso es de una empresa que fabrica 4 referencias de producto. 
## En cada orden de pedido se especifica una referencia, una cantidad a pedir de 
## cada referencia y una fecha de entrega. La fábrica comienza a operar a las 
## 6:00 y termina de operar a las 24:00. Solo se puede trabajar durante esos 
## intervalos de tiempo. Las entregas de pedidos a un cliente se realizan a las 
## 8:00 máximo del dia de la entega. La producción de cada producto se hace enve 
## tres máquonas secuenciadas y consecutivas. El primer proceso es la preparación,
## el segundo es la fabricación y el último es el empaque. Los tiempos de cada 
## proceso para cada referencia son los siguientes: 

## --------------------------------------------------------------------------------------------- 
##  |          PREPARACIÓN              |        FABRICACIÓN      |       EMPAQUETAMIENTO    |
## ---------------------------------------------------------------------------------------------             
##  | Referencia	  Producto x Hora   |   Referencia	  Horas   |    Referencia	  Horas  |
##  |     1	                25          |       1           2     |        1            2    |
## 	|     2	                15          |       2           2     |        2            1    |
##	|     3	                30          |       3           2     |        3            1    |
## 	|     4	                25          |       4           2     |        4            1    |
## --------------------------------------------------------------------------------------------- 
## NOTA: para los procesos de fabricación y empaquetamiento el tiempo es
## independiente de a cantidad de órdenes de pedido.

## Adicionalmente, tenemos un tiempo de tardanza por cada tipo de referencia y
## un tiempo SETUP cuando se cambia de una máquina a otra. 

## -------------------------------------------            ----------------------- 
##  |           COSTOS POR TARDANZA          |            |   TIEMPOS DE SETUP  |
## -------------------------------------------            -----------------------
##  |  Referencia   |	Costo/hora por orden |            | * |   1   2   3   4 |
## -------------------------------------------            -----------------------
##  |      1	    |        $ 9.000         |            | 1 |   0   2   1   2 |
##  |      2	    |        $ 5.000         |            | 2 |   1   0   3   1 |
##  |      3	    |        $ 7.000         |            | 3 |   1   2   0   2 | 
##  |      4	    |        $ 10.000        |            | 4 |   2   2   1   0 |
## -------------------------------------------            -----------------------

## La información sobre cada orden de pedido es la siguiente

## ------------------------------------------------------------------
##  | Orden	  |   Referencia   |  Cuadernos   |  Fecha de Entrega  |
## ------------------------------------------------------------------
##  |   1     |	      1	       |      225	  |      07/05/2019    | 
##  |   2     |	      2	       |      150	  |      07/05/2019    | 
##  |   3     |	      3	       |      270	  |      08/05/2019    | 
##  |   4     |	      4	       |      175	  |      08/05/2019    | 
##  |   5     |	      1	       |      150	  |      09/05/2019    | 
##  |   6     |	      2	       |      90	  |      10/05/2019    | 
##  |   7     |	      3	       |      300	  |      10/05/2019    | 
##  |   8     |	      4	       |      200	  |      08/05/2019    | 
##  |   9     |	      1	       |      50	  |      11/05/2019    | 
##  |   10    |	      2	       |      150	  |      10/05/2019    | 
##  |   11    |	      3	       |      270	  |      10/05/2019    | 
##  |   12    |	      4	       |      225	  |      12/05/2019    | 
##  |   13    |	      1	       |      225	  |      11/05/2019    | 
##  |   14    |	      2	       |      150	  |      11/05/2019    | 
##  |   15    |	      3	       |      150	  |      13/05/2019    | 
##  |   16    |	      4	       |      175	  |      13/05/2019    | 
##  |   17    |	      1	       |      150	  |      15/05/2019    | 
##  |   18    |	      2	       |      135	  |      14/05/2019    | 
##  |   19    |	      3	       |      300	  |      14/05/2019    | 
##  |   20    |	      4	       |      125	  |      14/05/2019    | 
## -----------------------------------------------------------------


import sys
import datetime
from datetime import timedelta
import copy

def calcular_makespan(secuencia, tiempo_preparacion_ord, tiempo_fabricacion_ord, tiempo_empaque_ord, SETUP, fecha_inicio_produccion, referencias):
    
    tiempo_actual_m1 = copy.deepcopy(fecha_inicio_produccion)
    for i in range(0,20):
        print("--- O: ",secuencia[i],"---Ref:",referencias[secuencia[i]-1])
        
        trabajo = secuencia[i]
        
        if ( i > 0):
            
            t_SETUP = SETUP[referencias[secuencia[i-1]-1]-1][referencias[secuencia[i]-1]-1]
            t1 = tiempo_actual_m1 + timedelta( hours = t_SETUP )
            t2 = t1.day - tiempo_actual_m1.day #diferencia en días entre la terminación del trabajo y la fecha actual
            if ( tiempo_actual_m1.hour == 0 and tiempo_actual_m1.minute == 0): #Si sucede que el tiempo de la máquina 1 es 24:00
                tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = 6 )
                tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = t_SETUP )
            elif ( t2 == 0 or ( t2 == 1 and t1.hour == 0 ) ):
                tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = t_SETUP )
            else:
                dif = tiempo_actual_m1.hour - 6
                tiempo_actual_m1 = tiempo_actual_m1 + timedelta( days = 1 )
                tiempo_actual_m1 = tiempo_actual_m1 - timedelta( hours = dif )
                tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = t_SETUP )
            #fi
            print(t_SETUP)
            print(tiempo_actual_m1)
        #fi
        
        ## MÁQUINA 1
        t1 = tiempo_actual_m1 + timedelta( hours = tiempo_preparacion_ord[trabajo-1] )
        t2 = t1.day - tiempo_actual_m1.day #diferencia en días entre la terminación del trabajo y la fecha actual
        if ( tiempo_actual_m1.hour == 0 and tiempo_actual_m1.minute == 0): #Si sucede que el tiempo de la máquina 1 es 24:00
            tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = 6 )
            tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = tiempo_preparacion_ord[trabajo-1] )
        elif ( t2 == 0 or ( t2 == 1 and t1.hour == 0 ) ):
            tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = tiempo_preparacion_ord[trabajo-1] )
        else:
            dif = tiempo_actual_m1.hour - 6
            tiempo_actual_m1 = tiempo_actual_m1 + timedelta( days = 1 )
            tiempo_actual_m1 = tiempo_actual_m1 - timedelta( hours = dif )
            tiempo_actual_m1 = tiempo_actual_m1 + timedelta( hours = tiempo_preparacion_ord[trabajo-1] )
        #fi
        print(tiempo_actual_m1)
        
        
        ## MÁQUINA 2
        tiempo_actual_m2 = copy.deepcopy(tiempo_actual_m1)
        
        t1 = tiempo_actual_m2 + timedelta( hours = tiempo_fabricacion_ord[trabajo-1] )
        t2 = t1.day - tiempo_actual_m2.day #diferencia en días entre la terminación del trabajo y la fecha actual
        if ( tiempo_actual_m2.hour == 0 and tiempo_actual_m2.minute == 0): #Si sucede que el tiempo de la máquina 1 es 24:00
            tiempo_actual_m2 = tiempo_actual_m2 + timedelta( hours = 6 )
            tiempo_actual_m2 = tiempo_actual_m2 + timedelta( hours = tiempo_fabricacion_ord[trabajo-1] )
        elif ( t2 == 0 or ( t2 == 1 and t1.hour == 0 ) ):
            tiempo_actual_m2 = tiempo_actual_m2 + timedelta( hours = tiempo_fabricacion_ord[trabajo-1] )
        else:
            dif = tiempo_actual_m2.hour - 6
            tiempo_actual_m2 = tiempo_actual_m2 + timedelta( days = 1 )
            tiempo_actual_m2 = tiempo_actual_m2 - timedelta( hours = dif )
            tiempo_actual_m2 = tiempo_actual_m2 + timedelta( hours = tiempo_fabricacion_ord[trabajo-1] )
        #fi
        print(tiempo_actual_m2)
        
        
        ## MÁQUINA 3
        tiempo_actual_m3 = copy.deepcopy(tiempo_actual_m2)
        
        t1 = tiempo_actual_m3 + timedelta( hours = tiempo_empaque_ord[trabajo-1] )
        t2 = t1.day - tiempo_actual_m3.day #diferencia en días entre la terminación del trabajo y la fecha actual
        if ( tiempo_actual_m3.hour == 0 and tiempo_actual_m3.minute == 0): #Si sucede que el tiempo de la máquina 1 es 24:00
            tiempo_actual_m3 = tiempo_actual_m3 + timedelta( hours = 6 )
            tiempo_actual_m3 = tiempo_actual_m3 + timedelta( hours = tiempo_empaque_ord[trabajo-1] )
        elif ( t2 == 0 or ( t2 == 1 and t1.hour == 0 ) ):
            tiempo_actual_m3 = tiempo_actual_m3 + timedelta( hours = tiempo_empaque_ord[trabajo-1] )
        else:
            dif = tiempo_actual_m3.hour - 6
            tiempo_actual_m3 = tiempo_actual_m3 + timedelta( days = 1 )
            tiempo_actual_m3 = tiempo_actual_m3 - timedelta( hours = dif )
            tiempo_actual_m3 = tiempo_actual_m3 + timedelta( hours = tiempo_empaque_ord[trabajo-1] )
        #fi
        print(tiempo_actual_m3)
            
    #rof
#fed

def principal(argv):
    
    ## DATOS DE ENTRADA
    ordenes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    referencias = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    num_cuadernos = [225, 150, 270, 175, 150, 90, 300, 200, 50, 150, 270, 225, 225, 150, 150, 175, 150, 135, 300, 125]
    fecha_entrega = ['07/05/2019', '07/05/2019', '08/05/2019', '08/05/2019', '09/05/2019', '10/05/2019', '10/05/2019', '08/05/2019', '11/05/2019', '10/05/2019', '10/05/2019', '12/05/2019', '11/05/2019', '11/05/2019', '13/05/2019', '13/05/2019', '15/05/2019', '14/05/2019', '14/05/2019', '14/05/2019']
    fecha_entrega = [ datetime.datetime.strptime(x, '%d/%m/%Y') for x in fecha_entrega]
    costo_tardanza = [9000, 5000, 7000, 10000]
    SETUP = [[0, 2, 1, 2], [1, 0, 3, 1], [1, 2, 0, 2], [2, 2, 1, 0]]
    t_prep_ref = [25, 15, 30, 25]
    t_fab_ref = [2, 2, 2, 2]
    t_emp_ref = [2, 1, 1, 1]
    
    tiempo_preparacion_ord = []
    tiempo_fabricacion_ord = []
    tiempo_empaque_ord = []
    for i in range(len(ordenes)):
        tiempo_preparacion_ord.append(int(num_cuadernos[i]/t_prep_ref[referencias[i]-1]))
        tiempo_fabricacion_ord.append(t_fab_ref[referencias[i]-1])
        tiempo_empaque_ord.append(t_emp_ref[referencias[i]-1])
    #rof
    fecha_inicio_produccion = x = datetime.datetime(2019, 5, 6, 6,0) 
    print(tiempo_preparacion_ord, tiempo_fabricacion_ord, tiempo_empaque_ord)
    ## OBTECIÓN DE LA SECUENCIA
    secuencia = [1, 13, 19, 17, 9, 15, 7, 10, 14, 5, 3, 11, 6, 18, 2, 4, 8, 12, 16, 20]

    ## CALCULO DEL MAKESPAN
    makespan = calcular_makespan(secuencia, tiempo_preparacion_ord, tiempo_fabricacion_ord, tiempo_empaque_ord, SETUP, fecha_inicio_produccion, referencias)
    
#fed
    
if __name__ == "__main__":
    principal(sys.argv)
#fi