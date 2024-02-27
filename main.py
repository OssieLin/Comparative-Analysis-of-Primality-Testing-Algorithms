from graph import *
from primality_test import *
from miller_rabin_test import *

compare_primality_tests = [
    (lambda n: lucas_type_primality_test(n, 8, 6), "Lucas-Type Sequence(8,6)", 1),
    (lambda n: lucas_type_primality_test(n, 8, 6), "Lucas-Type Sequence(8,6) with 2-rough", 2),
    (lambda n: lucas_type_primality_test(n, 8, 6), "Lucas-Type Sequence(8,6) with 3-rough", 3)
]
plot_combined_graph_from_tests(compare_primality_tests)

c0_min = -40
c0_max = 60
c1_min = 0
c1_max = 100

n_values = list(range(1, 50))
# Fermat case
c0_values = [-n**2 for n in n_values]
c1_values = [2 * n for n in n_values]

#plt.plot(c0_values, c1_values, marker='o', linestyle='-', color='red', label='Fermat Case')

list_of_spp = [[log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, 3) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]
plt.imshow(list_of_spp, extent=(c0_min, c0_max, c1_min, c1_max))
colorbar = plt.colorbar()

plt.title('Logs of Lucas-Type Pseudoprimes up to 10000 with 3-rough')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max+1, 20))
plt.yticks(range(c1_min, c1_max+1, 20))
plt.show()

list_of_spp = [[log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, 2)for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]
plt.imshow(list_of_spp, extent=(c0_min, c0_max, c1_min, c1_max))  # Set the extent for x and y axes
plt.colorbar()
plt.title('Logs of Lucas-Type Pseudoprimes up to 10000 with 2-rough')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max+1, 20))
plt.yticks(range(c1_min, c1_max+1, 20))
plt.show()



list_of_log_spp=[[log_of_smallest_lucas_type_pseudoprime(c0, c1) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]
plt.imshow(list_of_log_spp, extent=(c0_min, c0_max, c1_min, c1_max))  # Set the extent for x and y axes
plt.colorbar()
plt.title('Numbers of Lucas-Type Pseudoprimes up to 1000')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max+1, 20))
plt.yticks(range(c1_min, c1_max+1, 20))
#plt.show()



#analyze_primality_test(cpn_primality_test, "CPN Primality Test", 1)
#analyze_primality_test(cpn_primality_test, "CPN Primality Test k=3", 3)
#analyze_primality_test(lambda n: lucas_type_primality_test(n, -9,6), "fermat 3", 2)


analyze_primality_test(lambda n: lucas_type_primality_test(n, 1, 2), "Lucas-Type Primality Test",1)

