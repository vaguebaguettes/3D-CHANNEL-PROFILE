import customtkinter as ctk
import numpy as np
from CTkTable  import *

my_file = open("materials.txt", "r") 
material = ""
thermcond = ""
thermdiff = ""

# reading the file 
data = my_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
Input= data.split("\n") 

 
temp = []
 
# Getting elem in list of list format
for elem in Input:
    temp2 = elem.split('/ ')
    temp.append((temp2))
 


# Initialize the output list
Output = []
for elem in temp:
    Output.append(elem)

print(Output) 

app = ctk.CTk()

app.grid_columnconfigure(0, pad=10)

app.title("Materials Selection Code")



print(Output)



table = CTkTable(master=app, row=7, column=3, values=Output)
table.pack(expand=True, fill="both", padx=20, pady=20)
table.grid(row=0,column=0)

# Callback function for the combobox
def combobox_callback2(choice):
    global material, thermcond, thermdiff
    if choice == "Polycarbonate":
        material, thermcond, thermdiff = Output[0]
    elif choice == "Soda-lime":
        material, thermcond, thermdiff = Output[1]
    elif choice == "Soda-lime HB":
        material, thermcond, thermdiff = Output[2]
    elif choice == "Quartz":
        material, thermcond, thermdiff = Output[3]
    elif choice == "Silica_web":
        material, thermcond, thermdiff = Output[4]
    elif choice == "Silica_book":
        material, thermcond, thermdiff = Output[5]
    elif choice == "H13":
        material, thermcond, thermdiff = Output[6]


combobox_var2 = ctk.StringVar(value="l")
plotbox = ctk.CTkComboBox(app, values=["Polycarbonate", "Soda-lime", "Soda-lime HB", "Quartz", "Silica_web", "Silica_book", "H13"], command=combobox_callback2, variable=combobox_var2)
plotbox.grid(row=1,column=0)
combobox_var2.set("Choose")

def button_event():
    file = open("tempmaterial.txt", "w")
    file.write(material + "/ " + thermcond +"/ "+ thermdiff) 
    file.write("\n")
    with open('verification.txt', 'w') as f:
        f.write('material done')
    print(material)
    app.destroy()

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Confirm",
                                 command=button_event)
button.grid(row=2,column=0)


app.mainloop()

    



