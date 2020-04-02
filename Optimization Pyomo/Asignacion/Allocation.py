import pyomo.environ as pyo
from pyomo.opt import SolverFactory

## ----------------------- MODELO -------------------------------
opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio128\\cplex\\bin\\x64_win64\\cplex")
#opt = SolverFactory('glpk')
model = pyo.AbstractModel()

## --------------------- CONJUNTOS ----------------------------
model.REF = pyo.Set()
model.RACKS = pyo.Set()

## ---------------------- PARÁMETROS ----------------------------
model.AnchoCaja = pyo.Param( model.REF )
model.TipoDist = pyo.Param( model.REF )
model.Espacios = pyo.Param( model.REF, mutable=True )
model.TipoRack = pyo.Param( model.RACKS )
model.Pared = pyo.Param( model.RACKS )
model.Utilizacion = pyo.Param( model.RACKS )

model.Demanda  = pyo.Param( model.REF )
model.Frecuencia  = pyo.Param( model.REF )
model.Costo = pyo.Param( model.RACKS )

## ---------------------- VARIABLES ----------------------------
model.x = pyo.Var( model.REF, model.RACKS, domain = pyo.Binary )
model.y = pyo.Var( model.RACKS, domain = pyo.Binary )

## ---------------------- FUNCIÓN OBJETIVO ----------------------------
def ObjFunc( model ):
    return sum(model.Demanda[ref]*model.Frecuencia[ref]*model.Costo[rack]*model.x[ref,rack] for ref in model.REF for rack in model.RACKS )
#fed
model.FO = pyo.Objective( rule = ObjFunc )

## ---------------------- RESTRICCIONES ----------------------------
def r1( model, ref ):
    return sum( model.x[ref,rack] for rack in model.RACKS ) == 1
#fed
model.r1 = pyo.Constraint( model.REF, rule = r1 )

def r2( model, rack ):
    return sum( model.AnchoCaja[ref]*model.x[ref,rack] for ref in model.REF ) <= 250*(1-model.y[rack]) + 750*(model.y[rack])
#fed
model.r2 = pyo.Constraint( model.RACKS, rule = r2)

def r3( model, ref, rack):
    return model.x[ref,rack] <= (model.y[rack]*model.TipoDist[ref]) + ((1-model.y[rack])*(1-model.TipoDist[ref]))
#fed
model.r3 = pyo.Constraint( model.REF, model.RACKS, rule = r3 )

def r6( model, ref, rack ):
    return model.Espacios[ref]*model.x[ref,rack] <= model.TipoRack[rack]
#fed
model.r6 = pyo.Constraint( model.REF, model.RACKS, rule = r6 )

def r8( model, rack ):
    return model.y[rack] <= 1 - model.Pared[rack]
#def
model.r8  = pyo.Constraint( model.RACKS, rule = r8 )
 
def r9( model, ref, rack ):
    return model.x[ref,rack] <= model.Utilizacion[rack]
#def
model.r9 = pyo.Constraint( model.REF, model.RACKS, rule = r9 )


## ============= Create a model instance and optimize =================
instance = model.create_instance('datos_tesis_542.dat')
opt.options['timelimit'] = 20
results = opt.solve(instance, tee = False)
#instance.display()
## ====================================================================

def print_result_console( instance ):
    print("\n\n")
    print("SOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("\n")
    print("Función Objetivo: ",pyo.value(instance.FO))
    print("\n")
    for ref in instance.REF:
        for rack in instance.RACKS:
            if ( instance.x[ref,rack] == 1 ):
                print("La referencia ", ref ," en el rack", rack)
            #fi
        #rof
    #rof
    print("Función Objetivo: ",pyo.value(instance.FO))
#fed
    
print_result_console( instance )