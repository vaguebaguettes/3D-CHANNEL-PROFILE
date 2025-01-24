
import os
import subprocess
import main_loop
import temporalprog as tem
from tkinter import filedialog
import csv
import linemeshaiz

def read_progress(file_path):
    """Reads progress value from a file."""
    with open(file_path, 'r') as f:
        percentage = int(f.read().strip())
        return percentage
    

def run_progress_bar_script():
    script_name = 'progress_bar_script_overall.py'
    if os.name == 'nt':  # Windows
        command = f'start cmd /k "python {script_name} & exit"'
        subprocess.Popen(command, shell=True)
    elif os.name == 'posix':  # Unix-like systems (Linux, MacOS)
        command = f'gnome-terminal -- bash -c "python3 {script_name}; exec bash"'
        subprocess.Popen(command, shell=True)
    else:
        print(f"Unsupported OS: {os.name}")


run_progress_bar_script()

size, array_y = tem.plotprep()
temploopi = tem.converted_result[11][1]
large_data =  [['y(linemesh)', 't(time)', 'z(linemesh)', 'T(temperature)']]
filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
with open(filepath, 'w') as csvfile:
        csvwriter =  csv.writer(csvfile)
        csvwriter.writerows(large_data)

z_array = linemeshaiz.linemesh(tem.converted_result[8][1], tem.converted_result[5][1])
zsize = read_progress("zsize.txt")
    
for i in range(zsize):
    i += 1
    z = z_array[i - 1]
    z *= -1
    file = main_loop.mainloop(z, temploopi, size, array_y, filepath)
    with open(filepath, 'a') as csvfile:
            csvwriter =  csv.writer(csvfile)
            csvwriter.writerow(["PLANE"])
    


    