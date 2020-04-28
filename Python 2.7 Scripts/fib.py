#!/usr/bin/python

import sys


def fib(n):

    if (n<2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    #fi


#fed
    
            
            

def main( argv ):
    n=int(raw_input("Digite numero: "))
    x=fib(n)
    print x
#fed
    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - rot13.py
