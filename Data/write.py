import sys
import os

## WRITE FILE WHIT FUNCTION OPEN
def principal( argv ):
    ## Management Fyles.
    ## Function open() is the function for read fyles in python
    ## open("demofile.txt", "rt") receive two parameters. 
    ## The first parameter is the file or the ubication of the file
    ## The second parameter is the method or mode. There are four modes.
    ## "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    ## "a" - Append - Opens a file for appending, creates the file if it does not exist
    ## "w" - Write - Opens a file for writing, creates the file if it does not exist. 
    ## If the file exist. Delete the content if we use x method
    ## "x" - Create - Creates the specified file, returns an error if the file exists

    file1 = open("write.txt","w")
    file1.write("primera linea")
    file1.write(" contiuacion segunda linea y salto de linea \n")
    file1.write("segunda linea \n")
    file1.close()
    

    filepath = 'write.txt'
    with open(filepath,"r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        #elihw
    #htiw

    ## -------------------------------
    print("---------------------------------")
    ## This part delete the old file
    Lines = ["first lin \n","second line \n","third line \n"]
    with open("write.txt","w") as f:
        for line in Lines:
            f.write(line)
        #rof
    #htiw

    
    
    filepath = 'write.txt'
    with open(filepath,"r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        #elihw
    #htiw

    ## -------------------------------
    print("---------------------------------")
    ## Edit the old file
    Lines = ["fourth lin \n","fifth line \n","sixth line \n"]
    with open("write.txt","a") as f:
        for line in Lines:
            f.write(line)
        #rof
    #htiw

    filepath = 'write.txt'
    with open(filepath,"r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        #elihw
    #htiw

    ## -------------------------------
    print("---------------------------------")

    # file1 = open("write2.txt","w")
    # file1.write("")
    # file1.close()

    ## This method remove a file of he folder
    if os.path.exists("write2.txt"):
        os.remove("write2.txt")
    #fi
    
    ## Create new file
    ## The method "a" edit a file if the file exist, an create a new file else
    Lines = ["fourth line \n","fifth line \n","sixth line \n"]
    with open("write2.txt","a") as f:
        for line in Lines:
            f.write(line)
        #rof
    #htiw

    filepath = 'write2.txt'
    with open(filepath,"r") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        #elihw
    #htiw

    ## -------------------------------
    print("---------------------------------")
    ## Create new file whit the method "x"
    
    if os.path.exists("write3.txt"):
        print("The file exist")
    else:
        Lines = ["fourth line \n","fifth line \n","sixth line \n"]
        with open("write3.txt","x") as f:
            for line in Lines:
                f.write(line)
            #rof
        #htiw

        filepath = 'write3.txt'
        with open(filepath,"r") as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
            #elihw
        #htiw
    #fi
#fed







if __name__ == "__main__":
    principal( sys.argv )
#fi