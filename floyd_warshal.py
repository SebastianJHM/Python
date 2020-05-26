import sys
import string
import numpy

def floyd_warshall(GRAPH):
    n = len(GRAPH)
    d = dict(enumerate(string.ascii_uppercase, 1))
    REC = []
    for i in range(n):
        r = []
        for j in range(n):
            if( i != j ):
                r.append(d[j+1])
            else:
                r.append("-")
            #fi
        #rof
        REC.append(r)
    #rof
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if( k!=i or k!=j ):
                    if(GRAPH[i][j] > GRAPH[k][j] + GRAPH[i][k]):
                        GRAPH[i][j] = GRAPH[k][j] + GRAPH[i][k]
                        REC[i][j] = d[k+1]
                    #fi
                #fi
            #rof
        #rof
        print("------ NODO ", d[k+1], "--------" )
        print(numpy.array(GRAPH))
        print(numpy.array(REC))
    #rof
    print(numpy.array(GRAPH))
    print(numpy.array(REC))
#fed

def principal(argv):
    I=100000
    GRAPH = [
        [0,4,2,I,I,I],
        [4,0,I,I,I,I],
        [2,I,0,1,2,I],
        [I,3,1,0,I,2],
        [I,I,2,3,0,4],
        [I,I,I,2,4,0],
    ]
    floyd_warshall(GRAPH)
#fed




if __name__ =="__main__":
    principal(sys.argv)
