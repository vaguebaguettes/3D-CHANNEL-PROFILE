import temporalprog as tem
import temp_loop as tploop
import csv
from tkinter import filedialog

def update_progress(file_path, percentage):
    with open(file_path, 'w') as f:
        f.write(str(percentage))

def mainloop(z, temploopi, size, array_y, filepath):

    
    for i in range(size):
        i += 1
        y = array_y[i - 1]
        t = tem.tprep()
        plotlist=[]
        plot_list = []
        plot_list = tploop.temploop(temploopi, y, t, plotlist, z)
        file_path = 'inner_progress.txt'
        progress_percentage = ((i + 1) / size) * 100
        update_progress(file_path, progress_percentage)
        with open(filepath, 'a') as csvfile:
            csvwriter =  csv.writer(csvfile)
            csvwriter.writerows(plot_list)
        
    return filepath
