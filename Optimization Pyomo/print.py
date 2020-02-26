# Pyomo v4.4.1
# Python 2.7
from pyomo.environ import *
from pyomo.opt import SolverFactory

a = 370
b = 420
c = 4

model             = ConcreteModel()
model.x           = Var([1,2], domain=Binary)
model.y           = Var([1,2], domain=Binary)
model.Objective   = Objective(expr = a * model.x[1] + b * model.x[2] + (a-b)*model.y[1] + (a+b)*model.y[2], sense=maximize)
model.Constraint1 = Constraint(expr = model.x[1] + model.x[2] + model.y[1] + model.y[2] <= c)

opt = SolverFactory('glpk')

results = opt.solve(model)

#
# Print values for each variable explicitly
#
print("Print values for each variable explicitly")
for i in model.x:
  print(str(model.x[i]), model.x[i].value)
for i in model.y:
  print(str(model.y[i]), model.y[i].value)
print("")

#
# Print values for all variables
#
print("Print values for all variables")
for v in model.component_data_objects(Var):
  print(str(v), v.value)

print(a * model.x[1].value + b * model.x[2].value + (a-b)*model.y[1].value + (a+b)*model.y[2].value)
for x in model.component_data_objects(Objective):
    print(x)
