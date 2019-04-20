
def pat1(rows): 
    for row in range(rows): 
        print("*"*row)
    
def pat2(rows): 
    for row in range(rows): 
        print(" "*row,end='')
        print("*"*(rows-row))