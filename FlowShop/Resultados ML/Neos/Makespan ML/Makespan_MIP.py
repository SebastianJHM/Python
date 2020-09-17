import sys
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

def create_lineal_model_tardiness( model, TP, dd ):
    
    ## Número de trabajo y máquinas
    num_trabajos = len(TP)
    num_maquinas = len(TP[0])
    jobs = [i+1 for i in range(num_trabajos)]
    machines = [i+1 for i in range(num_maquinas)]
    
    ## --------------------- CONJUNTOS ----------------------------
    model.J = pyo.Set( initialize = jobs )
    model.M = pyo.Set( initialize = machines )
    model.P = pyo.Set( initialize = jobs )
    
    ## ## ---------------------- PARÁMETROS ----------------------------
    def paramTP(model, j, m):
        return(TP[j-1][m-1])
    #fed
    model.T_Proc = pyo.Param(model.J,model.M, initialize = paramTP)
    def paramDD(model, j):
        return(dd[j-1])
    #fed
    model.Due_Dates = pyo.Param(model.J, initialize = paramDD)
    
    ## ---------------------- VARIABLES ----------------------------
    model.x = pyo.Var(model.J, model.P, domain = pyo.Binary)
    model.T_Inicio = pyo.Var(model.P, model.M)
    model.T_Final = pyo.Var(model.P, model.M)
    model.Makespan = pyo.Var()
    
    model.T_Terminacion = pyo.Var(model.J)
    model.Tardanza = pyo.Var(model.J, within=pyo.NonNegativeReals)
    model.Tardanza_Total = pyo.Var()
    ## ---------------------- FUNCIÓN OBJETIVO ----------------------------
    def ObjFunc( model ):
        return model.Makespan
    #fed
    model.FO = pyo.Objective( rule = ObjFunc )
    
    ## ---------------------- RESTRICCIONES ----------------------------
    def r1( model, j ):
        return sum( model.x[j,p] for p in model.P ) == 1
    #fed
    model.r1 = pyo.Constraint( model.J, rule = r1 )
    
    def r2( model, p ):
        return sum( model.x[j,p] for j in model.J ) == 1
    #fed
    model.r2 = pyo.Constraint( model.P, rule = r2 )
    
    def r3( model, p, m ):
        return model.T_Final[p,m] == model.T_Inicio[p,m] + sum( model.x[j,p]*model.T_Proc[j,m] for j in model.J )
    #fed
    model.r3 = pyo.Constraint( model.P, model.M, rule = r3 )
    
    def r4( model, p, m ):
        if ( m > 1 ):
            return model.T_Inicio[p,m] == model.T_Final[p,m-1]
        return pyo.Constraint.Skip
    #fed
    model.r4 = pyo.Constraint( model.P, model.M, rule = r4 )
    
    def r5( model, p, m ):
        if ( p > 1 ):
            return model.T_Inicio[p,m] >= model.T_Final[p-1,m]
        return pyo.Constraint.Skip
    #fed
    model.r5 = pyo.Constraint( model.P, model.M, rule = r5 )
    
    def r6( model ):
        return model.T_Inicio[1,1] == 0
    #fed
    model.r6 = pyo.Constraint( rule = r6 )
    
    def r7( model ):
        return model.Makespan == model.T_Final[len(model.J), len(model.M)]
    #fed
    model.r7 = pyo.Constraint( rule = r7 )
    
    def r8( model, j, p ):
        return model.T_Terminacion[j] >= model.T_Final[p, len(model.M)] - 100000*(1-model.x[j,p])
    #fed
    model.r8 = pyo.Constraint( model.J, model.P, rule = r8 )
    
    def r9( model, j, p ):
        return model.T_Terminacion[j] <= model.T_Final[p, len(model.M)] + 100000*(1-model.x[j,p])
    #fed
    model.r9 = pyo.Constraint( model.J, model.P, rule = r9 )
    
    def r10( model, j ):
        return model.Tardanza[j] >= model.T_Terminacion[j] - model.Due_Dates[j]
    #fed
    model.r10 = pyo.Constraint( model.J, rule = r10 )
    
    def r11( model, j, p ):
        return model.Tardanza_Total == sum(model.Tardanza[j] for j in model.J)
    #fed
    model.r11 = pyo.Constraint( model.J, model.P, rule = r11 )
    
    return(model)
#fed

def print_results_console( instance ):
    print("\nSOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("Makespan: ", round(pyo.value(instance.Makespan)))
    print("Tardanza: ", round(pyo.value(instance.Tardanza_Total)))
    secuencia = []
    for p in instance.P:
        for j in instance.J:
            if ( instance.x[j,p] == 1 ):
                secuencia.append(j)
            #fi
        #rof
    #rof
    print("Secuencia: ",secuencia)
    
    print("--------------------------")
    for p in instance.P:
        print("\nPosición ", p, end=" .... ")
        for j in instance.J:
            if ( instance.x[j,p] == 1 ):
                print("Trabajo: ", j)
            #fi
        #rof
        for m in instance.M:
            print("Tiempo de inicio: ", round(pyo.value(instance.T_Inicio[p,m])), "--> Tiempo_Final: ", round(pyo.value(instance.T_Final[p,m])))
        #rof
    #rof
    
    for j in instance.J:
        print("\nTrabajo ", j, ": \nTerminación: ", round(pyo.value(instance.T_Terminacion[j])), " --> Tardanza: ", round(pyo.value(instance.Tardanza[j])))
    #rof
#fed

def obtener_resultados(instance):
    secuencia = []
    for p in instance.P:
        for j in instance.J:
            if ( instance.x[j,p] == 1 ):
                secuencia.append(j)
            #fi
        #rof
    #rof
    return(secuencia, round(pyo.value(instance.Makespan)), round(pyo.value(instance.Tardanza_Total)))
#fed

def modelo_makespan( TP, dd ):
    ## DECLARE SOLVER, CREATE A PYOMO ABSTRACT MODEL, DECLARE LINEAR MODEL
    #opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio1210\\cplex\\bin\\x64_win64\\cplex")
    # opt = SolverFactory("gurobi", solver_io="python")
    # opt = SolverFactory('glpk', executable="C:\\Users\\USUARIO1\\Desktop\\Programas\\Gusek\\GUSEK PRINCIPAL\\glpsol")
    
    opt = pyo.SolverManagerFactory('neos')
    model = pyo.AbstractModel()
    model = create_lineal_model_tardiness( model, TP, dd )
    
    ## Crear una instancia del modelo y ejecutarla
    instance = model.create_instance()
    results = opt.solve(instance, opt='mosek', tee = False)
    #instance.display()
    
    secuencia, makespan, tardanza = obtener_resultados(instance)
    return(secuencia, makespan, tardanza)
   
#fed