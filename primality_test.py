from math import log
from pseudoprime_counter import *
from util import *

def analyze_primality_test(primality_test, primality_test_name,k ):
    counter = PseudoprimeCounter(primality_test, primality_test_name,k)
    counter.count_pseudoprimes(k)
    counter.plot_graph()
    counter.print_pseudoprimes()

def cpn_primality_test(n):
    a = 2
    b = 6
    for _ in range(n-2):
        c = (2*b + a) % n
        a = b
        b = c
    # Check if number passes the cpn Primality test
    return (b-2) % n == 0



def smallest_lucas_type_pseudoprime(c0, c1, max=1000):
    for n in range(2, max):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1):
            return n
    return max

def log_of_smallest_lucas_type_pseudoprime(c0, c1):
    for n in range(2, 1000):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1):
            return log(n)
    return log(1000)

def smallest_lucas_type_pseudoprime_up_to(c0, c1):
    counter = 0
    for n in range(2, 1000):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1) :
            counter += 1
    return counter

def lucas_type_primality_test(n, c0, c1):
    a = 2
    b = c1
    for _ in range(n - 1):
        c = (c1 * b + c0 * a) % n
        a = b
        b = c
    # Check if number passes the cpn Primality test
    return (b - c1) % n == 0

def fermat_primality_test(n, c):#fermat's little theorem
    return pow(c, n - 1, n) == 1

print(fermat_primality_test(3, 66))
