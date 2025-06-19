

def printNmubers(num:int):
    '''
        The function receives a specific number and then prints it in descending pyramidal order.
    '''
    r:str = ""
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            r += " " + str(j)
        r += "\n"
    
    print(r)
        
printNmubers(5)