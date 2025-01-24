import numpy as np
import func
import matplotlib.pyplot as plt

def linemesh(div, y):
    i = 0
    resp_var = 0
    linemesh_y = []
    while True:

        false = ((i+1)/100)*div
        bool = resp_var >= (y/2)*0.3
        result_1 = func.select(div, false, bool)
        bool = (resp_var + result_1) >= (y/2)
        if bool == True:
            result_2 = (y/2)
            linemesh_y.append(result_2)
            break

        append_var = resp_var + result_1
        resp_var = append_var
        print(resp_var)
        linemesh_y.append(append_var)
        i += 1


    return linemesh_y

# Example usage:
