
#!/usr/bin/python

import sys

## -------------------------------------------------------------------------
def ObtenerSuposicion( ):
    G = []
    while True:
        print("Adivine un numero de cuatro digitos: ",)
        S = input( )
        G = []
        for i in range( len( S ) ):
            G.append( int( S[ i ] ) )
        # rof
        if len( G ) == 4:
            break
        else:
            print("Intente de nuevo... ",)
        # fi
    # elihw
    return(G)
# fed

## -------------------------------------------------------------------------
def ContarFijas( N, G ):
    f = 0
    for i in range( len( N ) ):
        if N[ i ] == G[ i ]:
            f = f + 1
        # fi
    # rof
    return f
# fed

## -------------------------------------------------------------------------
def ContarPicas( N, G ):
    p = 0
    for i in range( len( N ) ):
        found = False
        j = 0
        while ( j < len( G ) ) and ( not found ):
            found = ( N[ i ] == G[ j ] ) and ( i != j )
            j = j + 1
        # elihw
        if found:
            p = p + 1
        # fi
    # rof
    return p
# fed

## -------------------------------------------------------------------------
def Retador_PicasYFijas( N ):
    c = 0
    f = 0
    p = 0
    while True:
        G = ObtenerSuposicion( )
        c = c + 1
        f = ContarFijas( N, G )
        p = ContarPicas( N, G )
        print("Picas:", p)
        print("Fijas:", f)
        if f == 4:
            break
        # fi
    # elihw
    return c
# fed

## -------------------------------------------------------------------------
def main( argv ):

    ## Crear numero a adivinar
    N = [ 1, 2, 3, 4 ]

    ## Jugar
    c = Retador_PicasYFijas( N )

    ## Mostrar los resultados
    print("Adivino en", c, "intentos.")

#fed
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
