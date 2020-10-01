import sys
import os
import datetime

def principal(argv):
    
    ## Create file with de open method for delete with os
    open("file.txt", "x")
    
    ## Delete file
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    
    ## Create file with de open method for rename with os
    if not os.path.exists("file2.txt"):
        open("file2.txt", "x")
    
    ## Rename file if not exist the name
    if not os.path.exists("file2_renamed.txt"):
        os.rename("file2.txt", "file2_renamed.txt")
        
    ## Get the size of a filr in bytes
    x = os.path.getsize("system_information.py")
    print(x)
    
    ## Get the date of the last modification
    x = os.path.getmtime("system_information.py")
    print(datetime.datetime.fromtimestamp(x))
    
    ## Get the absolute path
    x = os.path.abspath("sytem_information.py")
    print(x)
    
    ## Directorio en el que se está trabajando
    x = os.getcwd()
    print(x)
    
    ## Create new directory
    if not os.path.exists("nuevo_directorio"):
        os.mkdir("nuevo_directorio")
    
    ## Change of directory
    os.chdir("nuevo_directorio")
    print(os.getcwd())
    
    ## Remove directory
    os.mkdir("nd")
    os.rmdir("nd")
    
    path = "C:\\Users\\USUARIO1\\Desktop\\MyPython"
    ## List files and directories
    x = os.listdir(path)
    print(x)
    
    ## Know if is file or directory
    print("========")
    for name in os.listdir(path):
        fullname = os.path.join(path, name)
        if os.path.isdir(fullname):
            print("{} is directory".format(name))
        if os.path.isfile(fullname):
            print("{} is file".format(name))
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi