# This is the entry point of our software

import sys
from add import add
from sub import sub
from mul import mul
from div import div

def getUserInput():
    x = input("Enter x: ")
    y = input("Enter y: ")
    op = input("""Select operator: 
    1 for '+'
    2 for '-'
    3 for 'x'
    4 for '/'
    """)
    return [x,y,op]

def output(result):
    print "The result is:", result

if __name__ == "__main__":
    print "Hello Dummy Cal!"
    
    # get input from user
    result = None
    while result is None:
        (x, y, op) = getUserInput()
        if op == 1: result = add(x, y)
        elif op == 2: result = sub(x, y)
        elif op == 3: result = mul(x, y)
        elif op == 4: result = div(x, y)
        else: print "Please enter a valid operator"
    
    # output result.
    output(result)





