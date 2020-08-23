import sys
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

def create_lineal_model_tardiness( model, TP ):
    
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
    
    ## ---------------------- VARIABLES ----------------------------
    model.x = pyo.Var(model.J, model.P, domain = pyo.Binary)
    model.T_Inicio = pyo.Var(model.P, model.M)
    model.T_Final = pyo.Var(model.P, model.M)
    model.Makespan = pyo.Var()
    
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
#fed

def print_results_console( instance ):
    print("\nSOLUCIÓN DEL EJERCICIO")
    print("--------------------------")
    print("Makespan: ",round(pyo.value(instance.FO)))
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
#fed

def principal( argv ):
    ## TP[t][m]: tiempo de procesamiento del trabajo t en la máquina m.
    TP = [
        [1, 13, 6, 2],
        [10, 12, 18, 18],
        [17, 9, 13, 4],
        [12, 17, 2, 6],
        [11, 3, 5, 16]
    ]
    
    TP = [
        [27, 79, 22, 93, 38],
        [92, 23, 93, 22, 84],
        [75, 66, 62, 64, 62],
        [94, 5, 53, 81, 10],
        [18, 15, 30, 94, 11],
        [41, 51, 34, 97, 93],
        [37, 2, 27, 54, 57],
        [58, 81, 30, 82, 81],
        [56, 12, 54, 11, 10],
        [20, 40, 77, 91, 40],
        [2, 59, 24, 23, 62],
        [39, 32, 47, 32, 49],
        [91, 16, 39, 26, 90],
        [81, 87, 66, 22, 34],
        [33, 78, 41, 12, 11],
        [14, 41, 46, 23, 81],
        [88, 43, 24, 34, 51],
        [22, 94, 23, 87, 21],
        [36, 1, 68, 59, 39],
        [65, 93, 50, 2, 27]
    ]


    ## DECLARE SOLVER, CREATE A PYOMO ABSTRACT MODEL, DECLARE LINEAR MODEL
    #opt = SolverFactory('cplex', executable="C:\\Program Files\\IBM\\ILOG\\CPLEX_Studio1210\\cplex\\bin\\x64_win64\\cplex")
    #opt = SolverFactory('glpk', executable="C:\\Users\\USUARIO1\\Desktop\\Programas\\Gusek\\GUSEK PRINCIPAL\\glpsol")
    # opt = SolverFactory("gurobi", solver_io="python")
    opt = pyo.SolverManagerFactory('neos')
    model = pyo.AbstractModel()
    create_lineal_model_tardiness( model, TP )
    
    ## Crear una instancia del modelo y ejecutarla
    instance = model.create_instance()
    # opt.solve(instance, tee = False)
    opt.solve(instance, opt='cplex', tee = False)
    #instance.display()
    
    print_results_console( instance )
#fed


if __name__ == "__main__":
    principal(sys.argv)
#fi