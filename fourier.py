

import math

'''

Variables!

a = is the number of times to loop the fourier series
i = is the iteration number. basically the same but im paranoid
pi = the constant pi pf mathematics 
b = is the squareroot of sumthin( a part of the Sn equation)
c = is a part of the series equation
d = is a part of the series equation
'''

import fourier_calc as fc

pi = math.pi
exp = math.e

def fourier(loop, tau, to, U, alpha, x, y, Si, t, z):
    loop += 1
    zero = 0
    for i in range(int(loop)):
        
        i += 1
        n = i

        series = fc.compute_series(x, y, z, n, Si, tau, t, to, U, alpha,)

        zero += series
        
    return zero
