from pyomo.environ import *
from pyomo.opt import SolverFactory



n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
o = [1, 2, 3, 4, 5]
ref = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
ordenesExcel = {1: [0, 4, 26, 1, 15, 18, 9, 33, 40, 11], 2: [0, 1, 7, 5, 15, 17], 3: [0, 4, 6, 1], 4: [0, 15, 18, 9], 5: [0, 4, 6, 1, 15, 18, 9, 8]}
rExcel = {1: [4, 26, 1, 15, 18, 9, 33, 40, 11], 2: [1, 7, 5, 15, 17], 3: [4, 6, 1], 4: [15, 18, 9], 5: [4, 6, 1, 15, 18, 9, 8]}
dist = [[0, 30, 33, 35, 28, 44, 49, 29, 48, 32, 37, 43, 22, 40, 27, 39, 43, 29, 38], [30, 0, 43, 43, 43, 44, 48, 29, 28, 22, 44, 49, 29, 45, 42, 45, 31, 22, 38], [33, 43, 0, 45, 47, 30, 50, 45, 40, 33, 21, 30, 38, 32, 40, 39, 32, 35, 43], [35, 43, 45, 0, 45, 33, 46, 29, 47, 41, 32, 41, 45, 44, 43, 33, 43, 34, 42], [28, 43, 47, 45, 0, 37, 32, 31, 28, 35, 21, 44, 21, 42, 43, 25, 33, 38, 41], [44, 44, 30, 33, 37, 0, 44, 32, 31, 32, 29, 21, 21, 41, 29, 35, 42, 20, 43], [49, 48, 50, 46, 32, 44, 0, 46, 20, 49, 38, 44, 37, 42, 45, 50, 35, 29, 27], [29, 29, 45, 29, 31, 32, 46, 0, 29, 50, 36, 34, 29, 25, 42, 43, 25, 24, 37], [48, 28, 40, 47, 28, 31, 20, 29, 0, 38, 38, 26, 32, 43, 47, 31, 28, 30, 35], [32, 22, 33, 41, 35, 32, 49, 50, 38, 0, 30, 38, 35, 22, 26, 35, 22, 43, 37], [37, 44, 21, 32, 21, 29, 38, 36, 38, 30, 0, 48, 42, 27, 31, 36, 50, 39, 28], [43, 49, 30, 41, 44, 21, 44, 34, 26, 38, 48, 0, 33, 49, 37, 40, 28, 49, 32], [22, 29, 38, 45, 21, 21, 37, 29, 32, 35, 42, 33, 0, 45, 31, 21, 39, 45, 30], [40, 45, 32, 44, 42, 41, 42, 25, 43, 22, 27, 49, 45, 0, 26, 40, 29, 37, 50], [27, 42, 40, 43, 43, 29, 45, 42, 47, 26, 31, 37, 31, 26, 0, 47, 46, 38, 36], [39, 45, 39, 33, 25, 35, 50, 43, 31, 35, 36, 40, 21, 40, 47, 0, 29, 25, 38], [43, 31, 32, 43, 33, 42, 35, 25, 28, 22, 50, 28, 39, 29, 46, 29, 0, 47, 34], [29, 22, 35, 34, 38, 20, 29, 24, 30, 43, 39, 49, 45, 37, 38, 25, 47, 0, 20], [38, 38, 43, 42, 41, 43, 27, 37, 35, 37, 28, 32, 30, 50, 36, 38, 34, 20, 0]]
ubic = {0: 0, 1: 4, 2: 15, 3: 4, 4: 9, 5: 18, 6: 9, 7: 14, 8: 10, 9: 17, 10: 16, 11: 11, 12: 18, 13: 15, 14: 4, 15: 7, 16: 18, 17: 18, 18: 11, 19: 17, 20: 18, 21: 15, 22: 3, 23: 4, 24: 1, 25: 18, 26: 11, 27: 18, 28: 7, 29: 2, 30: 5, 31: 8, 32: 8, 33: 11, 34: 10, 35: 4, 36: 2, 37: 3, 38: 9, 39: 14, 40: 11}

## Indicación de Solver
opt = SolverFactory('glpk')

model = AbstractModel()

## Conjuntos ------------------------------------------------------------------------
model.NODOS = Set( initialize = n )
model.O = Set( initialize = o )
model.REF = Set( initialize = ref )
def setORDENES(model, i):
    return(ordenesExcel[i])
#fed
model.ORDENES = Set(model.O, initialize = setORDENES)
def setR(model, i):
    return(rExcel[i])
#fed
model.R = Set(model.O, initialize = setR)



def junte(model):
    return((o,i,j) for o in model.O for i in model.ORDENES[o] for j in model.ORDENES[o] )
#fed
model.OROR = Set(dimen =3, initialize = junte )

def junte2(model):
    return((o,i) for o in model.O for i in model.ORDENES[o] )
#fed
model.OX = Set(dimen = 2, initialize = junte2 )

def junte3(model):
    return((o,i,j) for o in model.O for i in model.R[o] for j in model.R[o] )
#fed
model.ORR = Set(dimen = 3, initialize = junte3 )

def junte4(model):
    return((o,i) for o in model.O for i in model.R[o] )
#fed
model.OR  = Set(dimen = 2, initialize = junte4 )


## Parámetros -------------------------------------------------------------------------------
def paramDistancia(model, i, j):
    return(dist[i][j])
#fed
model.Distancia = Param(model.NODOS,model.NODOS, initialize = paramDistancia)
def paramNodRef(model, i):
    return(ubic[i])
#fed
model.Nod_Ref = Param(model.REF, initialize = paramNodRef) 

def dinit(model, i ,j):
    return model.Distancia[model.Nod_Ref[i],model.Nod_Ref[j]]
#fed
model.Distancia_R = Param(model.REF,model.REF, initialize = dinit,mutable = True)

## Variables ---------------------------------------------------------------------------------
model.x = Var(model.OROR, domain = Binary)
model.aux = Var(model.OR)
model.Dist_ORD = Var(model.O)


## Función Objetivo ---------------------------------------------------------------------------------
def ObjFunc(model):
    return sum(model.Distancia_R[i,j]*model.x[o,i,j] for o in model.O for i in model.ORDENES[o] for j in model.ORDENES[o])
#fed
model.FO = Objective(rule = ObjFunc)


## Restricciones ---------------------------------------------------------------------------------
def r1(model, o, i):
    return sum( model.x[o,i,j] for j in model.ORDENES[o]) == 1
#fed
model.r1 = Constraint( model.OX, rule = r1 )

def r2(model, o, j):
    return sum( model.x[o,i,j] for i in model.ORDENES[o]) == 1
#fed
model.r2 = Constraint( model.OX,  rule = r2 )

def r3(model, o, i):
    return model.x[o,i,i] == 0
#fed
model.r3 = Constraint( model.OX,  rule = r3 )

def r4(model, o, i, j):
    if ( i != j ):
        return model.aux[o,i] - model.aux[o,j] + len(model.R[o])*model.x[o,i,j] <= len(model.R[o]) - 1 
    return Constraint.Skip
#fed
model.r4 = Constraint( model.ORR,  rule = r4 )

def r5(model, o):
    return model.Dist_ORD[o] == sum( model.x[o,i,j]*model.Distancia_R[i,j] for i in model.ORDENES[o] for j in model.ORDENES[o] )
#fed
model.r5 = Constraint( model.O, rule = r5)

## Create a model instance and optimize
instance = model.create_instance() 
results = opt.solve(instance, timelimit = 2)
#instance.display()






## Impresión de Resultados
def imprimir_resultados():
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Distancia Total: ",value(instance.FO))
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

imprimir_resultados()