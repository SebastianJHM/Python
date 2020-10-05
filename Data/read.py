import sys


def principal( argv ):
    ## Management Fyles.
    ## Function open() is the function for read fyles in python
    ## open("demofile.txt", "rt") receive two parameters. 
    ## The first parameter is the file or the ubication of the file
    ## The second parameter is the method or mode. There are four modes.
    ## "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    ## "a" - Append - Opens a file for appending, creates the file if it does not exist
    ## "w" - Write - Opens a file for writing, creates the file if it does not exist
    ## "x" - Create - Creates the specified file, returns an error if the file exists


    print("========== 1")
    temp = open('read.txt','r').readlines()
    print(temp)

    print("========== 2")
    file1  = open('read.txt','r')
    temp = file1.read().splitlines()
    print(temp)

    print("========== 3")
    ## Read Lines while
    ## The advantages ow with is that we don't have to close the file
    filepath = 'read.txt'
    with open(filepath,"r") as fp:
        line = fp.readline()
        print(line)
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        #elihw
    #htiw

    print("========== 4")
    ## Read file for
    filepath = 'read.txt'
    with open(filepath) as fp:
        for cont, line in enumerate(fp):
            print("Line {}: {}".format(cont, line))
        #elihw
    #htiw
    
    print("========== 5")
    ## Read file for
    filepath = 'read.txt'
    with open(filepath) as fp:
        for line in fp:
            print(line)
        #elihw
    #htiw

    print("========== 6")
    ## Read file for
    filepath = 'read.txt'
    with open(filepath) as fp:
        for line in fp:
            print(line.strip())
        #elihw
    #htiw
    
    print("========== 7")
    ## Read file readlines() vs readline()
    ## readline(): read the first line that was appointed
    ## readlines(): read the rest
    filepath = 'read.txt'
    with open(filepath) as fp:
        a = fp.readline()
        print(a)
        a = fp.readline()
        print(a)
        b = fp.readlines()
        print(b)
    #htiw

    print("========== 8")
    filepath = 'read.txt'
    with open(filepath) as fp:
        ## Read the first 3 chracters
        a = fp.readline(3)
        print(a)
        ## Read the next 4 characters
        a = fp.readline(4)
        print(a)
    #htiw
    fp.close()
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi