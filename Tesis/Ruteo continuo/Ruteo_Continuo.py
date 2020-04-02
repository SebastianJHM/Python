## Librerías propias de Pyomo
from pyomo.environ import *
from pyomo.opt import SolverFactory


## Indicación de Solver
opt = SolverFactory('glpk')

## ----------------------- MODELO -------------------------------
model = AbstractModel()

## Conjuntos
model.NODOS = Set()
model.ORDEN = Set()
model.R = Set()

## Parámetros
model.Distancia = Param(model.NODOS,model.NODOS)

## Variables
model.x = Var(model.ORDEN, model.ORDEN, domain=Binary)
model.aux = Var(model.R)

## Función Objetivo
def ObjFunc(model):
    return sum(model.Distancia[i,j]*model.x[i,j] for i in model.ORDEN for j in model.ORDEN)
#fed
model.FO = Objective(rule = ObjFunc)

## Restricciones
def r1(model, j):
    return sum(model.x[i,j] for i in model.ORDEN) == 1
#fed
model.r1 = Constraint(model.ORDEN, rule = r1 )

def r2(model, i):
    return sum(model.x[i,j] for j in model.ORDEN) == 1
#fed
model.r2 = Constraint(model.ORDEN, rule = r2 )

def r3(model, i):
    return model.x[i,i] == 0
#fed
model.r3 = Constraint(model.ORDEN, rule = r3 )

def r4(model, i, j):
    if ( i != j):
        return model.aux[i] - model.aux[j] + len(model.R)*model.x[i,j] <= len(model.R) - 1 
    return Constraint.Skip
    #fi
#fed
model.r4 = Constraint(model.R, model.R, rule = r4)

# Create a model instance and optimize
instance = model.create_instance('rc.dat') 
opt.options['tmlim'] = 12
results = opt.solve(instance)

#instance.display()

## Impresión de Resultados
print("\n\n")
print("SOLUCIÓN DEL EJERCICIO")
print("--------------------------")
print("\n")
print("Distancia Total: ",value(instance.FO))
print("\n")
print("De que nodo a que nodo: ")
print("--------------------------")
for i in instance.ORDEN:
    for j in instance.ORDEN:
        if ( instance.x[i,j].value == 1):
            print("Del nodo ",i," al nodo",j)
        #fi
    #rof
#rof


## OTRA FORMA DE IMPRMIR
# for i in instance.x: 
#     if (instance.x[i] == 1):
#         print("de ",i[0]," a ",i[1])
#     #fi
# #rof


# pyomo solve Ruteo_Continuo.py rc.dat --solver=glpk