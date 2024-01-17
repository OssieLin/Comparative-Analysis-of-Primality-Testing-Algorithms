import matplotlib.pyplot as plt

default_limit = 20
def is_prime(n):  # trial division
    if n < 2 or n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

class PseudoPrimeCounter:

    limit = default_limit

    def __init__(self, primality_test, primality_test_name, pre_sequence_length):
        self.primality_test = primality_test
        self.list_of_pseudo_prime = []
        self.accumulated_pseudo_prime_values = []
        self.primality_test_name = primality_test_name
        self.pre_sequence_length = pre_sequence_length

    def count_pseudo_primes(self):
        for n in range(self.pre_sequence_length, self.limit + 1):
            if self.primality_test(n):
                if not is_prime(n):
                    self.list_of_pseudo_prime.append(n)
            self.accumulated_pseudo_prime_values.append(len(self.list_of_pseudo_prime))

    def print_pseudo_primes(self):
        print(f"\nAll pseudo primes of {self.primality_test_name}: {self.list_of_pseudo_prime}")
        print(f"\nNumber of pseudo primes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudo_prime)}")

    def plot_graph(self, x_interval=1):
        x_values = range(self.pre_sequence_length, self.pre_sequence_length + len(self.accumulated_pseudo_prime_values))
        plt.plot(x_values, self.accumulated_pseudo_prime_values, marker='o')
        plt.title('Cumulative Number of Pseudo Primes vs Numerical Sequence of '+ self.primality_test_name, fontdict={'fontsize':8})
        plt.xlabel('Number in Numerical Sequence')
        plt.ylabel('Cumulative Number of Pseudo Primes')
        plt.grid(True)
        plt.xticks(range(0, len(self.accumulated_pseudo_prime_values) + self.pre_sequence_length, x_interval))
        plt.show(block=True)

#I'm trying to adjust the pseudo_prime test according to different primality test, but i'm not sure how to make the sequence right
"""
    def is_prime(self):
        return n == 2 or pow(2, n - 1, n) == 1
    def count_pseudo_primes(self):
        for n in range(self.sequence_length, self.limit + 1):
            if self.primality_test(n):
                if not self.is_prime(n):
                    self.list_of_pseudo_prime.append(n)
            self.accumulated_pseudo_prime_values.append(len(self.list_of_pseudo_prime))
    def print_pseudo_primes(self):
        print(f"\nAll pseudo primes of {self.primality_test_name}: {self.list_of_pseudo_prime}")
        print(f"\nNumber of pseudo primes up to {self.limit} of {self.primality_test_name}: {len(self.list_of_pseudo_prime)}")
"""