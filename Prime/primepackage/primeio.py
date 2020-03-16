#!/usr/bin/python

def write_primes(l, file_name):

    """reads a list of prime numbers and a file name. write the numbers from the list into the file"""

    with open(file_name, 'w') as f:
        writer = f.write(str(l));

def read_primes(file_name):

    """reads a file and generates a list"""

    with open(file_name, 'r') as f:
        reader = f.read();
        print(reader);

