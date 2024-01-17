import matplotlib.pyplot as plt
from pseudo_prime_counter import PseudoPrimeCounter, is_prime
kk
def cpnPrimalityTest(n):
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
        if not is_prime(n) and lucasTypePrimalityTest(n, c0, c1):
            return n
def lucasTypePrimalityTest(n, c0, c1):
    a = 2
    b = c1
    for _ in range(n - 1):
        c = (c1 * b + c0 * a) % n
        a = b
        b = c
    # Check if number passes the cpn Primality test
    return (b - c1) % n == 0
#list_of_spp=[smallest_lucas_type_pseudo_prime(1, c1) for c1 in range (2,10)]
list_of_spp=[[smallest_lucas_type_pseudo_prime(c0, c1) for c0 in range(2,5)] for c1 in range (2,10) ]
print( list_of_spp)
plt.imshow(list_of_spp)
plt.colorbar()
plt.show()
for c1 in range (2,10):
    print(smallest_lucas_type_pseudo_prime(1, c1))

counter = PseudoPrimeCounter(cpnPrimalityTest,"Companion Pell Number Primality Test",2)
counter.count_pseudo_primes()
counter.plot_graph()
counter.print_pseudo_primes()


counter2 = PseudoPrimeCounter(lambda n: lucasTypePrimalityTest(n, 1,2 ),"lucasTypePrimalityTest ",2)
counter2.count_pseudo_primes()
counter2.plot_graph()
counter2.print_pseudo_primes()


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
