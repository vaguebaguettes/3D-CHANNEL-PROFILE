import pandas as pd
import temporalprog as tp

def pulse(filename):
    cols = pd.read_csv(filename)
    ycol = 'y'
    for i in range(int(tp.converted_result[10][1]) - 1):
        cols[ycol] += (tp.prf * (i + 1))

        cols.to_csv(filename, mode='a', index=False, header=False)
        

        
