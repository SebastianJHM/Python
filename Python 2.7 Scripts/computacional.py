class persona:
  nombre=""
  edad=0
 
n= int(raw_input("Numero personas: "))

personas=[]

for j in range(n):
  personas.append("")

for j in range (len(personas)):
  personas[j]=persona()

for j in range(len(persona)):
  personas[j].edad = raw_input("ingrese edad ",i+1," :")
  x=-90000000
for i in range(len(persona)):
    if personas[i].edad > a :
      x=personas[i].edad
    break

print "el mas viejo tiene ", x ,  " anos"
