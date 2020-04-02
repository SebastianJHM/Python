## Librerías propias de Pyomo
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import sys

def imprimir_resultados(instance):
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Distancia Total: ",pyo.value(instance.FO))
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
#fed
            
def create_model(model):
    ## Conjuntos
    model.NODOS = pyo.Set()
    model.ORDEN = pyo.Set()
    model.R = pyo.Set()
    
    ## Parámetros
    model.Distancia = pyo.Param(model.NODOS,model.NODOS)
    
    ## Variables
    model.x = pyo.Var(model.ORDEN, model.ORDEN, domain=pyo.Binary)
    model.aux = pyo.Var(model.R)
    
    ## Función Objetivo
    def ObjFunc(model):
        return sum(model.Distancia[i,j]*model.x[i,j] for i in model.ORDEN for j in model.ORDEN)
    #fed
    model.FO = pyo.Objective(rule = ObjFunc)
    
    ## Restricciones
    def r1(model, j):
        return sum(model.x[i,j] for i in model.ORDEN) == 1
    #fed
    model.r1 = pyo.Constraint(model.ORDEN, rule = r1 )
    
    def r2(model, i):
        return sum(model.x[i,j] for j in model.ORDEN) == 1
    #fed
    model.r2 = pyo.Constraint(model.ORDEN, rule = r2 )
    
    def r3(model, i):
        return model.x[i,i] == 0
    #fed
    model.r3 = pyo.Constraint(model.ORDEN, rule = r3 )
    
    def r4(model, i, j):
        if ( i != j):
            return model.aux[i] - model.aux[j] + len(model.R)*model.x[i,j] <= len(model.R) - 1 
        return pyo.Constraint.Skip
        #fi
    #fed
    model.r4 = pyo.Constraint(model.R, model.R, rule = r4)
    
#fed
            
def principal( argv ):
    ## Indicación de Solver
    ## Con el optimizador de gusek
    opt = SolverFactory('glpk', executable="C:\\Users\\USUARIO1\Desktop\\Programas\\Gusek\\GUSEK PRINCIPAL\\glpsol")

    ## Create a model
    model = pyo.AbstractModel()
    
    ## Write the model
    create_model(model)
    
    # Create a instance and optimize
    instance = model.create_instance('rc.dat') 
    opt.options['tmlim'] = 12
    opt.solve(instance, tee=False)
    #instance.display()
    
    imprimir_resultados(instance)
#fed
        
if __name__ == "__main__":
    principal( sys.argv )
#fi