from math import log10
from pseudoprime_counter import *
from util import *

def analyze_primality_test(primality_test, primality_test_name,k_rough ):
    counter = PseudoprimeCounter(primality_test, primality_test_name,k_rough)
    counter.count_pseudoprimes(k_rough)
    counter.plot_graph()
    counter.print_pseudoprimes()

def cpn_primality_test(n):
    a = 2
    b = 6
    for _ in range(n-2):
        c = (2*b + a) % n
        a = b
        b = c
    return (b-2) % n == 0


def lucas_type_primality_test(n, c0, c1):
    a = 2 # a = V0
    b = c1 # b = V1
    for _ in range(n - 1):
        c = (c1 * b + c0 * a) % n
        a = b
        b = c
    return (b-c1) % n == 0

def fermat_primality_test(n, c):# fermat's little theorem
    return pow(c, n - 1, n) == 1

def smallest_lucas_type_pseudoprime(c0, c1, k_rough, pp_max):
    for n in range(2, pp_max+1):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1) and is_k_rough(n,k_rough):
            return n
    return pp_max

def log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, k_rough, pp_max):
    for n in range(2, pp_max+1):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1) and is_k_rough(n, k_rough):
            return log10(n)
    return float('nan')

def number_of_lucas_type_pseudoprime_up_to(c0, c1, k_rough, pp_max):
    counter = 0
    for n in range(2, pp_max+1):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1) and is_k_rough(n, k_rough):
            counter += 1
    return counter

def log_of_number_of_lucas_type_pseudoprime_up_to(c0, c1, k_rough, pp_max):
    counter = 0
    for n in range(2, pp_max+1):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1) and is_k_rough(n, k_rough):
            counter += 1
    if counter <= 0:
        return float('nan')
    else:
        return log10(counter)
