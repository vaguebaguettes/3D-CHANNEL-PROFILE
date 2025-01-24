
import matplotlib.pyplot as plt
import numpy as np
i = 0
divnum = int(input("number of division please"))
dur = float(input("time duration of laser cutting"))
n = 0

meshx = np.array([n])
meshy = np.array([n])    


for i in range(divnum + 1):
    
    '''This is just adding the iteration number(thats starts from 0) with the product of time duration 
    and division number being divided'''
    b = n + (dur / divnum)

    '''b is y's own num and n is just the incrementation using the product'''
    meshy = np.append(meshy, b)

    '''iteration num is increased manually cuz i want to record the x from 1, not 0'''
    i += 1
    
    '''iteration num is added to x cuz x is just an incrementation of 1'''
    meshx = np.append(meshx, i)
    
    '''the n number is updated with the product'''

    n = b
print(meshx)
print(meshy)


plt.title("Line graph")
plt.plot(meshx, meshy, color="red")

plt.show()







