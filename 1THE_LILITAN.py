#import customtk 

#this is to launch the login page

#with open('verification.txt', 'r') as f:
#    activation = f.read()
#this is to double verify that you logged into the page

import readmaterials
#this is to run the page to choose the material one would want

with open('verification.txt', 'r') as a:
    material_verify = a.read()
#verify the material is chosen

if material_verify == 'material done':
    import main
    
    #collecting the parameters of whats going to be done
    
    import new_loop

    #runs the main loop which also runs the temperature loop which has the fourier series and temperature equations
    
    #import pulse_loop

    #pulse_loop.pulse(main_loop.file)

    #runs the pulse function which unless selected to have a higher number, wouldnt cause any differences to the file (now cutout for the profile simulation)

    #import temporalprog as tem


    #output = tem.respect(main_loop.file)

    #import plottercontour 

    #plottercontour.plot(output)

    #the visuals are cut out

        
        
