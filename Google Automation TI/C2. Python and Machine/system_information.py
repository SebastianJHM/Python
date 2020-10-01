import sys
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.total) * 100
    return free > 20

def check_cpu_usage():
    usage_cpu = psutil.cpu_percent(1)
    return usage_cpu < 75

def principal( argv ):
    ## Utilización del disco
    du = shutil.disk_usage("/")
    print(du)
    print((du.free / du.total) * 100)
   
    # ## Utilización de la cpu en un intervalo de timepo
    # print(psutil.cpu_percent(0.1))
    
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    else:
        print("EVERYTHING IS OK!")
#fed


if __name__ == "__main__":
    principal( sys.argv )
#fi