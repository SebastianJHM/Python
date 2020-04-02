## Librerías propias de Pyomo
import pyomo.environ as pyo
from pyomo.opt import SolverFactory



## ----------------------- MODELO -------------------------------
## Indicación de Solver
opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio1210\\cplex\\bin\\x64_win64\\cplex")
model = pyo.AbstractModel()

## ------------------- SETS --------------------------------
model.NODOS = pyo.Set()
model.O = pyo.Set()
model.ORDENES = pyo.Set(model.O)
model.R = pyo.Set(model.O)
model.REF = pyo.Set()

def junte(model):
    return((o,i,j) for o in model.O for i in model.ORDENES[o] for j in model.ORDENES[o] )
#fed
model.OROR = pyo.Set(dimen =3, initialize = junte )

def junte2(model):
    return((o,i) for o in model.O for i in model.ORDENES[o] )
#fed
model.OX = pyo.Set(dimen = 2, initialize = junte2 )

def junte3(model):
    return((o,i,j) for o in model.O for i in model.R[o] for j in model.R[o] )
#fed
model.ORR = pyo.Set(dimen = 3, initialize = junte3 )

def junte4(model):
    return((o,i) for o in model.O for i in model.R[o] )
#fed
model.OR  = pyo.Set(dimen = 2, initialize = junte4 )


## --------------------- PARAMETERS -------------------------------------
model.Distancia = pyo.Param(model.NODOS,model.NODOS)
model.Nod_Ref = pyo.Param(model.REF) 

def dinit(model, i ,j):
    return model.Distancia[model.Nod_Ref[i],model.Nod_Ref[j]]
#fed
model.Distancia_R = pyo.Param(model.REF,model.REF, initialize = dinit,mutable = True)

## ----------------------- VARIABLES ---------------------------------------
model.x = pyo.Var(model.OROR, domain = pyo.Binary)
model.aux = pyo.Var(model.OR)
model.Dist_ORD = pyo.Var(model.O)


## -------------------------- OBJECTIVE FUNCTION ------------------------------------
def ObjFunc(model):
    return sum(model.Distancia_R[i,j]*model.x[o,i,j] for o in model.O for i in model.ORDENES[o] for j in model.ORDENES[o])
#fed
model.FO = pyo.Objective(rule = ObjFunc)

## --------------------------- RESTRICTIONS ----------------------------------------------
def r1(model, o, i):
    return sum( model.x[o,i,j] for j in model.ORDENES[o]) == 1
#fed
model.r1 = pyo.Constraint( model.OX, rule = r1 )

def r2(model, o, j):
    return sum( model.x[o,i,j] for i in model.ORDENES[o]) == 1
#fed
model.r2 = pyo.Constraint( model.OX,  rule = r2 )

def r3(model, o, i):
    return model.x[o,i,i] == 0
#fed
model.r3 = pyo.Constraint( model.OX,  rule = r3 )

def r4(model, o, i, j):
    if ( i != j ):
        return model.aux[o,i] - model.aux[o,j] + len(model.R[o])*model.x[o,i,j] <= len(model.R[o]) - 1 
    return pyo.Constraint.Skip
#fed
model.r4 = pyo.Constraint( model.ORR,  rule = r4 )

def r5(model, o):
    return model.Dist_ORD[o] == sum( model.x[o,i,j]*model.Distancia_R[i,j] for i in model.ORDENES[o] for j in model.ORDENES[o] )
#fed
model.r5 = pyo.Constraint( model.O, rule = r5)

## ============== Create a model instance and optimize ==============
instance = model.create_instance('P_A_M_1.dat') 
opt.options['timelimit'] = 15
results = opt.solve(instance, tee = False)
#instance.display()
## ==================================================================

## Impresión de Resultados
def imprimir_resultados( instance ):
    
    results = []
    for o in instance.O:
        route = []
        for i in instance.ORDENES[o]:
            for j in instance.ORDENES[o]:
                if ( instance.x[o,i,j].value == 1 ):
                    route.append([i, j])
                #fi
            #rof
        #rof
        results.append(route)
    #rof
    print(results)
    
    ## Ordenar Recorridos
    for i in range(len(results)):
        result = [results[i][0]]
        for _ in range(len(results[i])-1):
            aux = result[len(result)-1]
            for r in results[i]:
                if ( r[0] == aux[1] ):
                    result.append(r)
                    break
                #fi
            #rof
        #rof
        results[i] = result
    #rof
    
    cont_route = []
    for r in results:
        f = []
        for x in r:
            f.append(instance.Nod_Ref[x[0]])
        #rof
        f.append(instance.Nod_Ref[0])
        cont_route.append(f)
    #rof
    
    
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO(RACKS a RACKS)")
    print("--------------------------")
    print("\n")
    print("Distancia Total: ", pyo.value(instance.FO))
    print("\n")
    for o in instance.O:
        print("--------- Orden ",o,"----------")
        print("Distancia Recorrida: ",instance.Dist_ORD[o].value)
        print("Ruta: ")
        for i in range(len(results[o-1])):
            if ( instance.Nod_Ref[results[o-1][i][1]] == 0 ):
                print("Del Rack ", instance.Nod_Ref[results[o-1][i][0]], " al rack ", instance.Nod_Ref[results[o-1][i][1]], "......Entrega embalador")
            else:
                print("Del Rack ", instance.Nod_Ref[results[o-1][i][0]], " al rack ", instance.Nod_Ref[results[o-1][i][1]], "......Referencia: ", results[o-1][i][1])
            #fi
        #rof
        print("\n")
        print("Ruta continua(Racks): ", cont_route[o-1])
        print("\n")
    #rof
    print("Distancia Total: ", pyo.value(instance.FO))
#fed


imprimir_resultados( instance )