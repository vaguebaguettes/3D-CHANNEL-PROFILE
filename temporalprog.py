import linemeshai
import numpy
import Si_Calculations as Si
import timegraphfunc as tgf
import func
import pandas as pd
import test_2 as convert
import multiplier as mp



def extract_variables_from_file(file_path):
        variables_list = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    if ":" in line:
                        key, value = line.split(":")
                        variables_list.append([key.strip(), value.strip()])
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        return variables_list

# Example usage:

file_path = "temporary.txt"
extracted_vars = extract_variables_from_file(file_path)
for var in extracted_vars:
    print(f"{var[0]}: {var[1]}")

def convert_nested_list_to_float(nested_list):
    result = []
    for sublist in nested_list:
        converted_sublist = []
        for item in sublist:
            try:
                converted_item = float(item)
                converted_sublist.append(converted_item)
            except ValueError:
                # If the conversion fails, keep the original string value
                converted_sublist.append(item)
                print("fail conversion" + item)
        result.append(converted_sublist)
    return result



converted_result = convert_nested_list_to_float(extracted_vars)
prf = 1 / converted_result[1][1]
U = 1000 * converted_result[3][1]
check1 = converted_result[13][1] == 0
fact = func.select(2, 4, check1)  

def respect(file_path2):
    
    check = converted_result[12][1] == 0
    ans = func.select(1, U, check)
    convert.extract_and_delete_column(file_path2, 'quick_edit.csv', 'y')
    mp.multiply_column('quick_edit.csv', 'new_quick_edit.csv', 'y', ans)

    output = mp.merge_csv_into_second_column('new_quick_edit.csv', file_path2)
    return output
    




def plotprep():

    y = linemeshai.linemesh(converted_result[8][1], converted_result[9][1])

    negy =  [-x for x in y]

    size = len(negy)
    return(size, negy)

def Si_prep():
    with open('tempmaterial.txt', 'r') as file:
        material_string = file.read().rstrip()  # Remove trailing newline if present

    components = material_string.split('/')
    material_name = components[0].strip()  # Extract the material name (as a string)
    material_value1 = float(components[1].strip())  # Extract the first float value
    scientific_notation = float(components[2].strip())
    vals = float(scientific_notation)
    vals = vals * 100000 
    #pleaase note that the data is changed from 8.13E-7 to 8.13 for space issues. 
    #Possible solution is doing an automation where hte number subtracts from 12. 
    # and use that as a the number of zeroes in the next multipplication. The original number 
    # is 1e12, but shortened to 1e5 to balance it out
    # New afiq: Basically the 8.13E-7 is way too long to be stored and plus the fact that in the end, 
    # it will be multiplied by 10^12. So its far better if the e-7 can be redacted. 
    # The 10^12 will be left of 10^5, while 8.13e-7 will be just 8.13. This willmess up calculations,
    # as any materials added needs to be multiplied with 10^7

    # Convert to a regular float
    Sign = Si.Si_Calc(vals, U, prf)
    return(vals, Sign, material_value1)

def tprep():
    t = tgf.time(int(converted_result[11][1]), prf)
    t = list(t)
    return(t)