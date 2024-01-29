import matplotlib.pyplot as plt
import seaborn as sns
from math import log
from pseudo_prime_counter import PseudoPrimeCounter, is_prime

def analyze_primality_test(primality_test, primality_test_name):
    counter = PseudoPrimeCounter(primality_test, primality_test_name)
    counter.count_pseudo_primes()
    counter.plot_graph()
    counter.print_pseudo_primes()
def cpn_primality_test(n):
    a = 2
    b = 6
    for _ in range(n-2):
        c = (2*b + a) % n
        a = b
        b = c
    # Check if number passes the cpn Primality test
    return (b-2) % n == 0

def smallest_lucas_type_pseudo_prime(c0, c1):
    for n in range(2, 1000):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1):
            return n
    return 1000

def log_of_smallest_lucas_type_pseudo_prime(c0, c1):
    for n in range(2, 1000):
        if not is_prime(n) and lucas_type_primality_test(n, c0, c1):
            return log(n)
    return log(1000)

def smallest_lucas_type_pseudo_prime_up_to(c0, c1):
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
#list_of_spp=[smallest_lucas_type_pseudo_prime(1, c1) for c1 in range (2,10)]
def is_3_smooth(n):
    return remove_factors_2_and_3(n) == 1

def remove_factors_2_and_3(n):
    while n%2 == 0:
        n=n//2
    while n%3 == 0:
        n=n//3
    return n
def generate_pseudo_prime_heatmap(c0_range, c1_range):
    list_of_spp = [[smallest_lucas_type_pseudo_prime(c0, c1) for c0 in c0_range] for c1 in c1_range]
    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=c0_range, yticklabels=c1_range)
    plt.title('Smallest Pseudo Prime Heatmap of Lucas-type sequence')
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()

c0_range = range(90,100)
c1_range = range(90,100)
generate_pseudo_prime_heatmap(c0_range, c1_range)

def generate_pseudo_prime_heatmap_up_to(c0_range, c1_range):
    list_of_spp = [[smallest_lucas_type_pseudo_prime_up_to(c0, c1) for c0 in c0_range] for c1 in c1_range]
    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=c0_range, yticklabels=c1_range)
    plt.title('Numbers of Pseudo Prime Heatmap of Lucas-type sequence up to')
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()
c0_range = range(2,10)
c1_range = range(2,10)
#generate_pseudo_prime_heatmap_up_to(c0_range, c1_range)

list_of_3_smooth = [n for n in range(1, 100) if is_3_smooth(n)]
print(list_of_3_smooth)

list_of_spp=[[log_of_smallest_lucas_type_pseudo_prime(c0, c1) for c0 in range(2,20)] for c1 in range (2,49) ]
print( list_of_spp)

plt.imshow(list_of_spp)
plt.colorbar()
plt.show()


analyze_primality_test(cpn_primality_test, "cpn primality test")

analyze_primality_test(lambda n: lucas_type_primality_test(n, 5, 2), "lucas_type_primality_test")

"""
def is_prime(n):#trial division
    if n < 2 or n % 2 == 0:
         return n == 2
    d = 3
    while d*d <= n:
         if n % d == 0:
             return False
         d += 2
    return True
    
    def dbzPrimalityTest(n):
    a = 1
    b = 3
    c = 4
    d = 11
    e = 16
    f = 30
    g = 78
    for _ in range(n-7):
        h = (g+f+d+4*a)%n
        a, b, c, d, e, f, g = b, c, d, e, f, g, h
    return (g - 1) % n == 0
    
def fermat_is_prime(n):#fermat's little theorem
    return n==2 or pow(2, n - 1, n) == 1

listOfpseudoprime=[]
accumulated_pseudo_prime_values = []

for n in range(2, limit + 1):
    if cpnPrimalityTest(n):
        if not is_prime(n):
            listOfpseudoprime.append(n)
    accumulated_pseudo_prime_values.append(len(listOfpseudoprime))


# Print the list of values
print(f"\nAll pseudo primes: {listOfpseudoprime}")
print(f"\nNumber of pseudo primes up to {limit}: {len(listOfpseudoprime)}")

# Generate the graph
x=range(2, limit+1)
plt.plot(x, accumulated_pseudo_prime_values, marker='o')
plt.title('Cumulative Number of Pseudo Primes vs Numerical Sequence')
plt.xlabel('Number in Numerical Sequence')
plt.ylabel('Cumulative Number of Pseudo Primes')
plt.grid(True)
plt.xticks(x)
plt.show()
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
