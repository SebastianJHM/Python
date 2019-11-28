import sys
 
def factorial( n ):
    if ( n == 0 or n == 1):
        r = 1
    else:
        r = 1
        for i in range(1,n+1):
            r = r * i
        #rof
    #fi
    return r
#fed 

def raiz( x ):
    initial = [(0.04,0.2),(1,1),(4,2),(9,3),(25,5),(49,7),(100,10),(400,20),(900,30),(4900,70),(10000,100)]

    minim = 100000000000000000

    for y in initial:
        a = abs( y[0] - x )
        if ( a < minim):
            minim = a
            pos = initial.index(y)
        #fi
    #rof

    print(pos)
    ## -----------------------------------------
    center = initial[pos][0]
    r_center = initial[pos][1]
    ## -----------------------------------------

    vec = []

    if ( x == 0 ):
        result = 0.0
    else:
        acum = r_center
        for i in range(1,120):
            if ( i == 1 ) :
                acum = acum + (1/2)*(x-center)*(1/(r_center**1))*(1/factorial(1))
            else:
                prod = 1/2
                for j in range(1,i):
                    prod = prod*((2*j-1)/2)
                #rof
                signo = ((-1)**(i+1))
                ev = 1 / (r_center**( 2 * i - 1 ))
                fact = 1 / factorial( i )
                acum = acum + signo * prod * ev * fact * ((x-center)**i)
            #fi
        #rof
        result = round(acum,10)
    #fi
    return result
#fed

def principal( argv ):
    x = 433
    print("El resultado con la función es: ", raiz(x))
    print("El resultado con Python es: ", round(x**(1/2),10))
#fed


if __name__ == "__main__":
    principal( sys.argv )
# fi