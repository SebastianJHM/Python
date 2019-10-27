import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #fed
    

#ssalc
    
class Person2:
    def __init__(self, name="", age=None):
        self.name = name
        self.age = age
    #fed
#ssalc 
    
def principal( argv ):
    
    ## Hay dos opciones, la pimera en la que es obligatorio definir los prametros iniciales
    ## y la segunda opcion que mediante el argumento None o definiendola en la entrada de la función
    
    print("-------------------")
    p1 = Person("John", 35)
    print(p1.name)
    print(p1.age)
    print(p1)

    
    print("-------------------")
    p2 = Person2()
    p2.name = "John"
    print(p2.name)
    print(p2.age)
    
    print("-------------------")
#fed




if __name__ == "__main__":
    principal( sys.argv )
#fi