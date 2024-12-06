import math as m 

def square_integer(num):
    if isinstance (num, int):
        return m.pow(num,2)
    else:
        return "Please enter a valid integer:"