from graph import *
from primality_test import *

'''
plot_combined_graph_from_tests([
    (cpn_primality_test, "Companion Pell Number", 1),
    (cpn_primality_test, "CPN with rough 43", 43)
])


plot_combined_graph_from_tests([
    (lambda n: lucas_type_primality_test(n, 5, 2), "Lucas-Type Sequence(5,2)", 1),
    (lambda n: lucas_type_primality_test(n, 5, 2), "Lucas-Type Sequence(5,2) with rough 2", 2)
])
'''

c0_range = range(2,11)
c1_range = range(2,11)

generate_pseudoprime_heatmap(c0_range, c1_range)

#generate_pseudoprime_heatmap_up_to(c0_range, c1_range)

list_of_3_smooth = [n for n in range(1, 100) if is_3_smooth(n)]


list_of_spp = [[smallest_lucas_type_pseudoprime(c0, c1) for c0 in range(-20, 51)] for c1 in range(-20, 51)]

# Convert the list to a numpy array
plt.imshow(list_of_spp, extent=(-20, 51, -20, 51))  # Set the extent for x and y axes
plt.colorbar()
plt.title('Numbers of Lucas-Type Pseudoprimes up to 1000')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.show()

#print(f"\nList of smallest pseudo prime of Lucas-Type sequence: {list_of_spp}")


list_of_log_spp=[[log_of_smallest_lucas_type_pseudoprime(c0, c1) for c0 in range(2,51)] for c1 in range (2,51) ]
plt.imshow(list_of_log_spp)
plt.colorbar()
plt.title('Logs of Smallest Lucas-Type Pseudoprimes')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
#plt.show()


#analyze_primality_test(cpn_primality_test, "CPN Primality Test", 1)
#analyze_primality_test(cpn_primality_test, "CPN Primality Test k=3", 3)
#analyze_primality_test(lambda n: lucas_type_primality_test(n, -9,6), "fermat 3", 2)


#analyze_primality_test(lambda n: lucas_type_primality_test(n, 5, 2), "Lucas-Type Primality Test")

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

