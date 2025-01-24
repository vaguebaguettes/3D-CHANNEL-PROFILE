import fourier
import temporalprog as tem
import tempformula as tf
import func
import csv
from tkinter import filedialog

list = []

# main_script.py


def temploop(temploopi, y, tarray, plotlist, z):
    
    for  i in range(int(temploopi)):
        vals, Sign, k = tem.Si_prep()
        k = k / 1000000
        t = tarray[1][i - 1]

        series = fourier.fourier(tem.converted_result[4][1], tem.converted_result[2][1], tem.prf, tem.U, vals, tem.converted_result[7][1], y, Sign, t, tem.converted_result[5][1])
        T = tf.calculate_T(tem.converted_result[7][1], y, z, 22, tem.converted_result[0][1], tem.fact, k, tem.U, vals, tem.prf, tem.converted_result[2][1], series)
        #ans = func.select(tem.converted_result[6][1], T, T >= tem.converted_result[6][1])
        
        list = []
        if not T <= tem.converted_result[6][1]:

            list.append(y)
            list.append(t)
            list.append(z)
            list.append(T)

        else:
            list.append(0)

        plotlist.append(list)
        
        

    return(plotlist)
