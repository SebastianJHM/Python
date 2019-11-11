## Librerías propias de Pyomo
import pyomo.environ as pyo
from pyomo.opt import SolverFactory



## ----------------------- MODELO -------------------------------
## Indicación de Solver
opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio128\\cplex\\bin\\x64_win64\\cplex")
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
instance = model.create_instance('picking.dat') 
opt.options['timelimit'] = 500
results = opt.solve(instance, tee = False)
#instance.display()
## ==================================================================

## Impresión de Resultados
def imprimir_resultados( instance ):
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Distancia Total: ", pyo.value(instance.FO))
    print("\n")
    for o in instance.O:
        print("--------- Orden ",o,"----------")
        print("Distancia Recorrida: ",instance.Dist_ORD[o].value)
        print("Ruta: ")
        for i in instance.ORDENES[o]:
            for j in instance.ORDENES[o]:
                if ( instance.x[o,i,j].value == 1):
                    print("Del nodo ",i," al nodo",j)
                #fi
            #rof
        #rof
    #rof
#fed


imprimir_resultados( instance )