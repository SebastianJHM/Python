#!/usr/bin/python

import random
import sys

def main( argv ):
    x=0
    for a in range( 9 ):
        for b in range( 9):
            for c in range( 9 ):
                for d in range( 9 ):
                    for e in range( 9 ):
                        for f in range( 9 ):
                            x=0
                            for g in range( 9 ):
                            x=100000*a+100000*b+10000*c+1000*d+100*e+10*f+g;
				if (a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and b!=c and b!=d and b!=e and b!=f and b!=g and c!=d and c!=e and c!=f and c!=g 	and d!=e and d!=f and d!=g and e!=f and d!=g and f!=g and x%a==0 and x%b==0 and x%c==0 and x%d==0 and x%e==0 and x%f==0 and x%g==0){
	 			    print x
                                #fi
                            #rof   
                        #rof
                    #rof   
                #rof
            #rof
        #rof
    #rof   
#fed
    
if __name__ == "__main__":
    main( sys.argv )
# fi

## eof - programa_prueba.py
