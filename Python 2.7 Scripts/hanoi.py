#!/usr/bin/python

import sys


def hanoi(origen,destino,auxiliar,n):

    if (n==1):
        print("Mueva de", origen , " a " ,destino)
    else:
        hanoi(origen,auxiliar,destino,n-1)
        print("Mueva de", origen , " a " ,destino)
        hanoi(auxiliar,destino,origen,n-1)
    #fi


#fed
    
            
            

def main( argv ):
    n=int(raw_input("Digite numero: "))
    origen="A"
    destino="C"
    auxiliar="B"
    hanoi(origen,destino,auxiliar,n)
#fed
    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - rot13.py
    
