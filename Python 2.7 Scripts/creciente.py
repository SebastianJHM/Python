#!/usr/bin/python
import sys


def main( argv ):
    S = [1,1,2,5,6,0]
    x=0
    for i in range (0,len(S)-1,1):
        if (S[i+1]<S[i]):
            x=1
        #fi
    #rof
    if (x==0):
        print "Es creciente"
    else:
        print "No es creciente"
    #fi
#fed

    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
