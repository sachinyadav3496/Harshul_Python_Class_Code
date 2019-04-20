def hello(name):
    print("Welcome mr. ",name[::-1])
    
def hi(name):
    print("Welocme mr. ",*name[::-1])
    

print("Thanks for using one.py file ")
if __name__ == "__main__" : 
    print("Hello World")
    print("Program name : ",__name__)
    hi('Guido Van Rossum')
    hello('Python')