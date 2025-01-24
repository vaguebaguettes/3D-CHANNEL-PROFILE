def error():
    print("hah?")
    exit()

def select(true_output, false_output, condition):
    """
    Simulates the behavior of the LabVIEW "Select" function.

    Args:
        condition: A Boolean value (True or False) or an integer (0 or 1).
        true_output: The desired output when the condition is TRUE.
        false_output: The desired output when the condition is FALSE.

    Returns:
        The selected output based on the condition.
    """
    if condition == True :
        return true_output
    elif condition == False :
        return false_output
    else:
        raise ValueError("Condition must be a Boolean value (True/False) or an integer (0/1).")



def truefalse(s):
    if (s == 1):
        return False
    elif(s == 0):
        return True
    else:
        error()


