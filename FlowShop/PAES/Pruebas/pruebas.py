import sys
from leer_instancias_pruebas import read_data_XLSX
import random
import funciones_objetivo_prueba as fo
import xlsxwriter

def solucion_aleatoria( n ):
    sol = []
    verifica = [False] * n
    for _ in range(n):
        x = random.randint(1, n)
        while( verifica[x-1] == True ):
            x = random.randint(1, n)
        #elihw
        sol.append(x)
        verifica[x-1] = True
    #rof
    return(sol)
#fed


def principal(argv):
    INSTANCIAS = read_data_XLSX()
    workbook = xlsxwriter.Workbook('Results_Pruebas.xlsx')
    for inst in INSTANCIAS:
        secuencia = solucion_aleatoria(len(inst.tiempos_procesamiento))
        tp = inst.tiempos_procesamiento
        dd = inst.due_dates
        makespan, make_mat_i, make_mat_f = fo.calcular_makespan_blocking_secuencia(secuencia, tp)
        tardanza, due_date_sec = fo.calcular_tardanza_blocking_secuencia(secuencia, tp, dd)
        
        ## Imprimir archivo
        nombre_hoja = "Inst"+str(INSTANCIAS.index(inst)+1)
        imprimir_XLSX(workbook, nombre_hoja, secuencia, makespan, make_mat_i, make_mat_f, tardanza, due_date_sec)
    #rof
    workbook.close()
#fed

def imprimir_XLSX(workbook, nombre_hoja, secuencia, makespan, make_mat_i, make_mat_f, tardanza, due_date_sec):
    worksheet = workbook.add_worksheet(nombre_hoja)
    
    worksheet.set_column(1, 1, 9.5)
    
    cell_format_bold = workbook.add_format({
        'bold': 1,
        'align': 'center',
        'valign': 'vcenter'})
    cell_format = workbook.add_format({'align': 'center'})
    
    row = 1
    col = 1
    worksheet.write(row, col, "Makespan", cell_format_bold)
    
    col += 1
    worksheet.write(row, col, makespan, cell_format)
    
    worksheet.write("E2", "Tardanza", cell_format_bold)
    worksheet.write("F2", tardanza, cell_format)
    
    row += 2
    col = 1
    worksheet.write(row, col, "Secuencia", cell_format_bold)
    
    row += 1
    for s in secuencia:
        worksheet.write(row, col, s, cell_format)
        col += 1
    #rof
        
    row += 2
    col = 1
    worksheet.merge_range(row, col, row, col+4, "Matriz Tiempos Inicio", cell_format_bold)
    worksheet.merge_range(row, col+len(make_mat_i[0])+1, row, col+len(make_mat_i[0])+5, "Matriz Tiempos Finales", cell_format_bold)
    worksheet.merge_range(row, col+2*len(make_mat_i[0])+2, row, col+2*len(make_mat_i[0])+3, "Due Dates(SEC)", cell_format_bold)
    
    row += 1
    for i in range(len(make_mat_i)):
        col = 1
        col2 = 2 + len(make_mat_i[i])
        for j in range(len(make_mat_i[i])):
            worksheet.write(row, col, make_mat_i[i][j], cell_format)
            col += 1
            
            worksheet.write(row, col2, make_mat_f[i][j], cell_format)
            col2 += 1
        #rof      
        worksheet.merge_range(row, col2+1,row, col2+2, due_date_sec[i], cell_format)
        row += 1
    #rof
            
#fed


if __name__ == "__main__":
    principal(sys.argv)
#fi