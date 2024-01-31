# A k rough number is a positive integer whose prime factors are all greater than or equal to k.
def is_k_rough(n,k):
    for i in range(2, k+1):
        if n % i == 0:
            return False
    return True

def is_k_pseudoprime(n,k):
    return is_k_rough(n) and not is_prime(n)

def primality_test_with_rough_pseudoprimes(primality_test, k):
    results = []
    for n in range(2, default_limit + 1):
        if primality_test(n) and is_k_pseudoprime(n, k):
            results.append(n)
    return results

def is_prime(n):  # trial division
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def is_3_smooth(n):
    return remove_factors_2_and_3(n) == 1

def remove_factors_2_and_3(n):
    while n%2 == 0:
        n=n//2
    while n%3 == 0:
        n=n//3
    return n

#def test_pseudoprimes():
 #   if


'''
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
            if self.primality_test(n) and is_k_rough(n, self.k):
                self.list_of_pseudoprime.append(n)
            self.accumulated_pseudoprime_values.append(len(self.list_of_pseudoprime))

    def print_rough_pseudoprimes(self):
        print(f"\nAll pseudoprimes of {self.primality_test_name}: {self.list_of_pseudoprime}")
        print(f"\nNumber of pseudoprimes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudoprime)}")

def cpn_with_rough_3(n):
    if cpn_primality_test(n) and is_k_pseudoprime(n, 3):
        return n

plot_combined_graph_from_tests(
    (cpn_primality_test, "Companion Pell Number"),
    (cpn_with_rough_3, "CPN with rough 3"),
)
'''