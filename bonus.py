

def printNmubers(num:int):
    '''
        The function receives a specific number and then prints it in descending pyramidal order.
    '''
    r:str = ""
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            r += " " + str(j)
        r += "\n"
    
    return r
        
result:str = printNmubers(5)
print(result)