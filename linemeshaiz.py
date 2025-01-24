
import func


def update_progress(file_path, percentage):
    with open(file_path, 'w') as f:
        f.write(str(percentage))

def linemesh(div, y):
    i = 0
    resp_var = 0
    linemesh_y = []
    while True:

        false = ((i+1)/50)*div
        bool = resp_var >= (y)*0.4
        result_1 = func.select(div, false, bool)
        bool = (resp_var + result_1) >= (y)
        
        if bool == True:
            result_2 = (y)  
            linemesh_y.append(result_2)
            break
            
        append_var = resp_var + result_1
        resp_var = append_var
        print(resp_var)
        linemesh_y.append(append_var)
        i += 1
        
    
    for i in range(len(linemesh_y)):
        linemesh_y[i] *= -1
        linemesh_y[i] -= -y
        linemesh_y[i] = round(linemesh_y[i], 2)

    linemesh_y.reverse()
    update_progress("zsize.txt", len(linemesh_y))
    print(linemesh_y)

    return linemesh_y

linemesh(1, 1)

# Example usage:
'''
The linemesh z is incomplete because the z value should
be subtracting the array. dont reallly know what that means,
so i'll just wait for file from mom to run the labview.


'''



