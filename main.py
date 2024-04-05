from graph import *
from primality_test import *
import numpy as np

compare_primality_tests = [
    (lambda n: lucas_type_primality_test(n, 5, 2), "Lucas-Type Sequence(5,2)", 3),
    (lambda n: lucas_type_primality_test(n, 8, 6), "Lucas-Type Sequence(8, 6)", 3),
    (lambda n: lucas_type_primality_test(n, 1, 2), "CPN (Lucas-Type (1,2))", 3)
]
plot_combined_graph_from_tests(compare_primality_tests)

c0_min = -60
c0_max = 41
c1_min = 0
c1_max = 101

c0_range = range(2,11)
c1_range = range(2,11)

generate_pseudoprime_heatmap_up_to(c0_range, c1_range, 3)
#generate_spp_heatmap(c0_range, c1_range, 3)



# Second plot: logs of smallest Lucas-Type Pseudoprimes up to 10000 with k=3
list_of_spp_k3 = [[log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, 3) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]

max_value_k3 = np.max(list_of_spp_k3)

plt.imshow(list_of_spp_k3, extent=(c0_min, c0_max, c1_min, c1_max))  # Set the extent for x and y axes
colorbar_k3 = plt.colorbar(shrink=0.9)

plt.title('Logs of Smallest 3-rough Pseudoprimes up to 100000')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max, 20))
plt.yticks(range(c1_min, c1_max, 20))
#plt.show()

n_values = list(range(1, 50))
# Fermat case
c0_values = [-n**2 for n in n_values]
c1_values = [2 * n for n in n_values]

plt.plot(c0_values, c1_values, marker='o', linestyle='-', color='red', label='Fermat Case')

list_of_spp_k1 = [[log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, 1) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]

min_value_k1 = np.min(list_of_spp_k1)

plt.imshow(list_of_spp_k1, extent=(c0_min, c0_max, c1_min, c1_max)) # Set the extent and color scale
colorbar_k1 = plt.colorbar(shrink=0.9)

plt.title('Logs of Smallest Pseudoprimes up to 100000')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max, 20))
plt.yticks(range(c1_min, c1_max, 20))
#plt.show()



list_of_npp = [[log_of_number_of_lucas_type_pseudoprime_up_to(c0, c1, 3, 10000) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)]
plt.imshow(list_of_npp, extent=(c0_min, c0_max, c1_min, c1_max))
plt.colorbar()
plt.title('Logs of Number of Lucas-Type Pseudoprimes up to 10000 with 3-rough')
plt.xlabel('Parameter c0')
plt.ylabel('Parameter c1')
plt.xticks(range(c0_min, c0_max ))
plt.yticks(range(c1_min, c1_max ))
#plt.show()

#analyze_primality_test(lambda n: lucas_type_primality_test(n, 1, 2), "Lucas-Type Primality Test",1)
