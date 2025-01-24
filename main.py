
import customtkinter as ctk

# Read the content from the file
with open("tempmaterial.txt", "r") as file:
    content = file.read()

# Split the content using the '/' delimiter
material, thermcond, thermdiff = content.strip().split('/')

# Print the extracted values
print(f"Material: {material}")
print(f"Thermal Conductivity: {thermdiff}")
print(f"Thermal Diffusivity: {thermcond}")


las = 0

#System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#App Frame
app = ctk.CTk()

app.grid_columnconfigure(0, pad=10)

app.title("Planar Isotherm Simulation")

#UI Elements

'''
---------------------------------------------------------------------------------------------------------------------------------------
First Column
'''

maintitle = ctk.CTkLabel(app, text="Planar Isotherm Simulation Code", font=("Helvetica", 20))
maintitle.grid(row=0,column=0)

#Title Text
title = ctk.CTkLabel(app, text="Process Parameters", font=("Helvetica", 17))
title.grid(row=1, column=0)

#Power variable
power_text = ctk.CTkLabel(app, text="Power(W)")
power_text.grid(row=2, column=0)
power_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
power_entry.grid(row=3, column=0)

#PRF variable
prf_text = ctk.CTkLabel(app, text="PRF(Hz)")
prf_text.grid(row=4, column=0)
prf_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
prf_entry.grid(row=5, column=0)

#Pulse duration variable
pulsedur_text = ctk.CTkLabel(app, text="Pulse duration(s)")
pulsedur_text.grid(row=6, column=0)
pulsedur_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
pulsedur_entry.grid(row=7, column=0)

#Ux variable
Ux_text = ctk.CTkLabel(app, text="Ux(mm/s)")
Ux_text.grid(row=8, column=0)
Ux_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
Ux_entry.grid(row=9, column=0)

#Laser position variable
laser_text = ctk.CTkLabel(app, text="Laser Position")
laser_text.grid(row=10, column=0)

def combobox_callback(choice):
    global las
    if choice == "On the surface":
        las = 0
    elif choice == "Inside the sample":
        las = 1

combobox_var = ctk.StringVar(value="laser")
laserbox = ctk.CTkComboBox(app, values=["On the surface", "Inside the sample"], command=combobox_callback, variable=combobox_var)
laserbox.grid(row=11, column=0)
combobox_var.set("Choose")

#Title Text
title2 = ctk.CTkLabel(app, text="Solution Parameters", font=("Helvetica", 17))
title2.grid(row=12, column=0)

#fourier term variable
fourierterm_text = ctk.CTkLabel(app, text="Number of terms in the Fourier Series")
fourierterm_text.grid(row=13, column=0)
fourierterm_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
fourierterm_entry.grid(row=14, column=0)

#Number of Pulses variable
pulsenum_text = ctk.CTkLabel(app, text="Number of pulses to focus on")
pulsenum_text.grid(row=15, column=0)
pulsenum_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
pulsenum_entry.grid(row=16, column=0)

#Divisions of laser cutting time variable
laserdiv_text = ctk.CTkLabel(app, text="Divisions of the laser cutting time")
laserdiv_text.grid(row=17, column=0)
laserdiv_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
laserdiv_entry.grid(row=18, column=0)

#Plot with respect to variable
plot_text = ctk.CTkLabel(app, text="Plot with respect to ")
plot_text.grid(row=19, column=0)

def combobox_callback2(choice):
    global plots
    if choice == "Time":
        plots = 0
    elif choice == "X axis":
        plots = 1

combobox_var2 = ctk.StringVar(value="laser")
plotbox = ctk.CTkComboBox(app, values=["Time", "X axis"], command=combobox_callback2, variable=combobox_var2)
plotbox.grid(row=20, column=0)
combobox_var2.set("Choose")

'''
---------------------------------------------------------------------------------------------------------------------------------------
Second Column
'''
#Power variable
material_text = ctk.CTkLabel(app, text="Material", font=("Helvetica", 14))
material_text.grid(row=2, column=1)
material_entry = ctk.CTkLabel(app, text=material)
material_entry.grid(row=3, column=1)

therm_text = ctk.CTkLabel(app, text="Thermal diffusivity (m^2/s) alpha = k/p*Cp", font=("Helvetica", 14))
therm_text.grid(row=4, column=1)
therm_entry = ctk.CTkLabel(app, text=thermdiff)
therm_entry.grid(row=5, column=1)

thermcon_text = ctk.CTkLabel(app, text="Thermal Conductivity", font=("Helvetica", 14))
thermcon_text.grid(row=6, column=1)
thermcon_entry = ctk.CTkLabel(app, text=thermcond)
thermcon_entry.grid(row=7, column=1)

rangey_text = ctk.CTkLabel(app, text="Range Y")
rangey_text.grid(row=13, column=1)
rangey_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
rangey_entry.grid(row=14, column=1)

divsize_text = ctk.CTkLabel(app, text="Division size")
divsize_text.grid(row=15, column=1)
divsize_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
divsize_entry.grid(row=16, column=1)

locx_text = ctk.CTkLabel(app, text="Location x")
locx_text.grid(row=17, column=1)
locx_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
locx_entry.grid(row=18, column=1)

locz_text = ctk.CTkLabel(app, text="Location z")
locz_text.grid(row=19, column=1)
locz_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
locz_entry.grid(row=20, column=1)

trunctemp_text = ctk.CTkLabel(app, text="Truncation Temp")
trunctemp_text.grid(row=21, column=1)
trunctemp_entry = ctk.CTkEntry(app, placeholder_text="Enter value")
trunctemp_entry.grid(row=22, column=1)


def auto_fill():
    fourierterm_entry.delete(0, ctk.END)
    fourierterm_entry.insert(0, "500")
    pulsenum_entry.delete(0, ctk.END)
    pulsenum_entry.insert(0, "1")
    laserdiv_entry.delete(0, ctk.END)
    laserdiv_entry.insert(0, "60")
    rangey_entry.delete(0, ctk.END)
    rangey_entry.insert(0, "400")
    divsize_entry.delete(0, ctk.END)
    divsize_entry.insert(0, "1")
    locx_entry.delete(0, ctk.END)
    locx_entry.insert(0, "1")
    locz_entry.delete(0, ctk.END)
    locz_entry.insert(0, "1")
    trunctemp_entry.delete(0, ctk.END)
    trunctemp_entry.insert(0, "20000")










def save_to_file():
    with open("temporary.txt", "w") as temp_file:
        temp_file.write(f"Power(W): {power_entry.get()}\n")
        temp_file.write(f"PRF(Hz): {prf_entry.get()}\n")
        temp_file.write(f"Pulse duration(s): {pulsedur_entry.get()}\n")
        temp_file.write(f"Ux(mm/s): {Ux_entry.get()}\n")
        temp_file.write(f"Fourier terms: {fourierterm_entry.get()}\n")
        temp_file.write(f"Locz: {locz_entry.get()}\n")
        temp_file.write(f"Trunctemp: {trunctemp_entry.get()}\n")
        temp_file.write(f"Locx: {locx_entry.get()}\n")
        temp_file.write(f"Divsize: {divsize_entry.get()}\n")
        temp_file.write(f"Rangey: {rangey_entry.get()}\n")
        temp_file.write(f"Number of Pulses: {pulsenum_entry.get()}\n")
        temp_file.write(f"Divisions of laser: {laserdiv_entry.get()}\n")
        temp_file.write(f"Plots with respect to: {plots}\n")
        temp_file.write(f"Laser position: {las}\n")



# Button event
def button_event():
    save_to_file()
    with open('verification.txt', 'w') as f:
        f.write('variables secured')
    print("Values saved to temporary.txt")
    app.destroy()


button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Confirm",
                                 command=button_event)
button.grid(row=22,  column=0)


autofill = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Auto-fill",
                                 command=auto_fill)
autofill.grid(row=22,  column=2)

#Functions


app.mainloop()