import matplotlib.pyplot as plt
from util import *

default_limit = 10000

class PseudoprimeCounter:

    limit = default_limit

    def __init__(self, primality_test, primality_test_name, k):
        self.primality_test = primality_test
        self.list_of_pseudoprime = []
        self.accumulated_pseudoprime_values = []
        self.primality_test_name = primality_test_name
        self.k=k

    def count_pseudoprimes(self, k):
        for n in range(2, self.limit + 1):
            if self.primality_test(n) and is_k_rough(n, k):
                if not is_prime(n):
                    self.list_of_pseudoprime.append(n)
            self.accumulated_pseudoprime_values.append(len(self.list_of_pseudoprime))


    def print_pseudoprimes(self):
        print(f"\nAll pseudoprimes of {self.primality_test_name}: {self.list_of_pseudoprime}")
        print(f"\nNumber of pseudoprimes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudoprime)}")
        l = [n for n in self.list_of_pseudoprime if is_3_smooth(n)]
        print(f"\nAll pseudoprimes that are 3_is_smooth of {self.primality_test_name}: {l}")

    def plot_graph(self, x_interval=100):
        x_values = range(2, 2 + len(self.accumulated_pseudoprime_values))
        plt.plot(x_values, self.accumulated_pseudoprime_values, marker='o')
        plt.title('Cumulative Number of Pseudoprimes vs Numerical Sequence of ' + self.primality_test_name, fontdict={'fontsize': 8})
        plt.xlabel('Number in Numerical Sequence')


#I'm trying to adjust the pseudo_prime test according to different primality test, but i'm not sure how to make the sequence correct
"""
    def is_prime(self):
        return n == 2 or pow(2, n - 1, n) == 1
    def count_pseudoprimes(self):
        for n in range(self.sequence_length, self.limit + 1):
            if self.primality_test(n):
                if not self.is_prime(n):
                    self.list_of_pseudoprime.append(n)
            self.accumulated_pseudoprime_values.append(len(self.list_of_pseudoprime))
    def print_pseudo_primes(self):
        print(f"\nAll pseudoprimes of {self.primality_test_name}: {self.list_of_pseudoprime}")
        print(f"\nNumber of pseudoprimes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudoprime)}")
"""