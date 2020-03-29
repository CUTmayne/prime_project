#!/usr/bin/python

"""functions to process numerical input"""

def isPrime(n):
    
    """reads a natural number n and returns true if it is a prime number and false elsewise"""
    result = False;
    if is_integer(n) == False:
        raise TypeError("Input is not an Integer.");
    elif n >= 0:
        raise ValueError("Input is zero or less.");
    elif n < 2:
        result = False;
    elif n == 2:
        result = True;
    else:
        for i in range(2, n):
            if i == n:
                return;
            elif n % i == 0:
                result = False;
                break;
            else:
                result = True;

    return result;

def getNPrime(num):
    
    """reads an integer num and returns a list containing the first n prime numbers"""

    counter = 0;
    token = 2;
    output = "Prime Numbers: ";

    while counter < num:
        if isPrime(token) == True:
            output += "\n" + str(token);
            counter += 1;
            token += 1;
        else:
            token += 1;

    return output;


