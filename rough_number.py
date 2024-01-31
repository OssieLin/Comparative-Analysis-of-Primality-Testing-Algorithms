import matplotlib.pyplot as plt
from pseudoprime_counter import is_prime
from main import cpn_primality_test, plot_combined_graph_from_tests

default_limit = 1000

# A k rough number is a positive integer whose prime factors are all greater than or equal to k.
def is_k_rough(n,k):
    for i in range(2, k+1):
        if n % i == 0:
            return True
    return False

def is_k_pseudoprime(n,k):
    return is_k_rough(n) and not is_prime(n)

def primality_test_with_rough_pseudoprimes(primality_test, k):
    for _ in range(2, default_limit + 1):
        if primality_test(n) and is_k_pseudoprime(n, k):
            return n
    return None
class RoughPseudoprimeCounter:
    limit = 1000

    def __init__(self, primality_test, primality_test_name, k):
        self.primality_test = primality_test
        self.k = k
        self.list_of_pseudoprime = []
        self.accumulated_pseudoprime_values = []
        self.primality_test_name = primality_test_name

    def count_rough_pseudoprimes(self, k):
        for n in range(2, self.limit + 1):
            if self.primality_test(n) and is_k_pseudoprime(n, self.k):
                self.list_of_pseudoprime.append(n)
            self.accumulated_pseudoprime_values.append(len(self.list_of_pseudoprime))

    def print_rough_pseudoprimes(self):
        print(f"\nAll pseudoprimes of {self.primality_test_name}: {self.list_of_pseudoprime}")
        print(f"\nNumber of pseudoprimes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudoprime)}")

cpn_with_rough_3 = primality_test_with_rough_pseudoprimes(cpn_primality_test, 3)

plot_combined_graph_from_tests(
    (cpn_primality_test, "Companion Pell Number"),
    (cpn_with_rough_3, "CPN with rough 3"),
)
