## Librerías propias de Pyomo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import random
import xlsxwriter


## ----------------------- MODELO -------------------------------
## Indicación de Solver
opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio128\\cplex\\bin\\x64_win64\\cplex")
model = AbstractModel()

## Conjuntos ------------------------------------------------------------------------
model.NODOS = Set()
model.O = Set()
model.ORDENES = Set(model.O)
model.R = Set(model.O)
model.REF = Set()

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
model.Distancia = Param(model.NODOS,model.NODOS)
model.Nod_Ref = Param(model.REF) 

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
instance = model.create_instance('picking.dat') 
results = opt.solve(instance, timelimit = 2)
#instance.display()

## --------------------- GUARDAR LOS RESULTADOS EN ARCHIVO EXCEL -----------------------------
    
# Crear libro y añadir un hoja
workbook = xlsxwriter.Workbook('Resultados.xlsx')

## Formatos
merge_format = workbook.add_format({
    'bold': 1,
    'align': 'center',
    'valign': 'vcenter'})

    
## Crear hoja
worksheet = workbook.add_worksheet('Resultados')
worksheet.set_column(0, 0, 30)

#worksheet.merge_range('A1:D1', "SOLUCIÓN DEL EJERCICIO", merge_format)
worksheet.merge_range(0, 0, 0, 3, "SOLUCIÓN DEL EJERCICIO", merge_format)

worksheet.write(1, 0, "Distancia Total: ")
worksheet.write(1, 1, value(instance.FO))

row=3
col=0
for o in instance.O:
    worksheet.write(row, col,"Orden ")
    worksheet.write(row, col + 1, o)
    row += 1

    worksheet.write(row, col,"Distancia Recorrida: ")
    worksheet.write(row, col + 1,instance.Dist_ORD[o].value)
    row += 1
    
    worksheet.write(row, col,"Ruta: ")
    row += 1
    
    for i in instance.ORDENES[o]:
        for j in instance.ORDENES[o]:
            if ( instance.x[o,i,j].value == 1):
                worksheet.write(row, col + 0,"Del nodo ")
                worksheet.write(row, col + 1,i)
                worksheet.write(row, col + 2," al nodo")
                worksheet.write(row, col + 3,j)
            #fi
        #rof
        row += 1
    #rof
#rof
    
# Hay que incluir workbook.close()
workbook.close()
##  -------------------------------------------------------------------------------------




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

for iteration in range(1,1):
    print("------------- ITERACION ",iteration," ------------------")

    x = []
    for i in range(0,41):
        x.append(random.randint(1, 18))
    #rof
    dictionary = dict(zip(range(0,41), x))
    dictionary[0] = 0
    print(dictionary)
    
    for i in instance.REF:
        for j in instance.REF:
            instance.Distancia_R[(i,j)] = instance.Distancia[dictionary[i],dictionary[j]]
        #rof
    #rof



    results = opt.solve(instance, timelimit =  2)




    imprimir_resultados()
#rof