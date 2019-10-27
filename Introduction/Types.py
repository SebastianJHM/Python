
import sys

## -------------------------------------------------------------------------
def principal( argv ):
    ## The function int convert a float to integers
    a = 12.5654
    print(int(a))

    ## The function float convert integers to floats
    a = 12
    print(float(a))

    ## The function str convert anythin to string
    a = 12
    print(str(a))

    ## Bool function
    a = True
    b = False
    c = bool(int(a) + int(b))
    d = bool(int(a) * int(b))
    print(int(a))
    print(int(b))
    print(c)
    print(d)

    ## Operation Variable
    x = 12
    y = x/5
    z = x//5
    print(y)
    print(z)

    ## Operations with strings
    x = "hola todos,"
    y = " como están"
    z = x + y
    print(z)
    print(z[0:2]) ## The first two characters of the string
    print(len(z)) ## The length of the string
    print(z.upper()) ## Conver string in a capital 
    w = z.replace("hola","buenas a")
    print(w)
#fed

if __name__ == "__main__":
    principal( sys.argv )
# fi