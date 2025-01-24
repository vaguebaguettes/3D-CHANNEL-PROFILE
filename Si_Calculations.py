import math
 

pi = math.pi

def Si_Calc(alpha, U, to):
    Si = (8*pi*alpha)/(to*U**2)
    return Si
