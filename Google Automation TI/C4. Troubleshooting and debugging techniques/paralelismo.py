## El siguiente script segmenta la CPU en n para copiar y pegar n archivos por
## separado de un folder a otro
import subprocess
from multiprocessing import Pool
import os

## Rendimiento 
# import psutil
# hecking CPU usage as well as the I/O and network bandwidth.
# psutil.cpu_percent()
# For checking disk I/O, you can use the following command:
# psutil.disk_io_counters()
# For checking the network I/O bandwidth:
# psutil.net_io_counters()

## Función de copiar y pegar
## En linux la librería que copia y pega es rsync
## En windows sería:
# import shutil
# src = "C:\\Users\\USUARIO1\\Downloads\\197687869.pdf"
# dest = "C:\\Users\\USUARIO1\\Desktop"
# shutil.copy2(src, dest)

def backup(src):
    dest = os.getcwd() + "/data/prod_backup/"
    print("Backing up {} into {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
    ## El método de Python getcwd () devuelve el directorio de trabajo 
    ## actual de un proceso.
    src = os.getcwd() + "/data/prod/"
    ## >> /home/student-00-c7a937fcea3d/data/prod/
    list_of_files = os.listdir(src)
    ## >> ['omega', 'sigma', 'delta', 'kappa', 'alpha', 'beta', 'gamma']
    
    all_files = []
    for value in list_of_files:
        full_path = os.path.join(src, value)
        all_files.append(full_path)
    ## >> ['/home/student-00-c7a937fcea3d/data/prod/omega', '/home/student-00-c7a937fcea3d/data/prod/sigma', '/home/student-00-c7a937fcea3d/data/prod/delta', '/home/student-00-c7a937fcea3d/data/prod/kappa', '/home/student-00-c7a937fcea3d/data/prod/alpha', '/home/student-00-c7a937fcea3d/data/prod/beta', '/home/student-00-c7a937fcea3d/data/prod/gamma']

    ## Pool(n) crea n distintos procesos de forma asincrona y paralela
    ## con map se hace la copia de cada archivo
    pool = Pool(len(all_files))
    pool.map(backup, all_files)