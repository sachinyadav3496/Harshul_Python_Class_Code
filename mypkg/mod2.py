
def hello(name):
    print("Hello mr. ",name)
    
    
add = lambda x,y : x + y 
sub = lambda x,y : x*y 


def prime(num): 
    counter = 2
    while counter <= num // 2 + 1 : 
        
        if num % counter == 0 : 
            return False
    else : 
        return True 