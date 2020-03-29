#!/usr/bin/python

"""A Python program generating a list of prime numbers and output them into a csv file"""

import primepackage
from primepackage import *

def main():
    """Generate 100 prime numbers and output it into output.csv file"""
    try:
        primes = getNPrime(100)
    except Exception as err:
        print("Catch error in main ...")
        raise
    try:
        write_primes(primes, 'output.csv')
    except Exception as err:
        print("Catch error in main ...")
        raise
    try:
        l = read_primes('output.csv')
    except Exception as err:
        print("Catch error in main ...")
        raise
    print(l)

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err.args, err);

