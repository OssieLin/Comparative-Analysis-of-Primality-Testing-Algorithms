from graph import *
from primality_test import *
import numpy as np

compare_primality_tests = [
    (lambda n: lucas_type_primality_test(n, 5, 2), "Lucas-Type Sequence(5,2)", 3),
    (lambda n: lucas_type_primality_test(n, 8, 6), "Lucas-Type Sequence(8, 6)", 3),
    (lambda n: lucas_type_primality_test(n, 1, 2), "CPN (Lucas-Type (1,2))", 3)
]
#plot_combined_graph_from_tests(compare_primality_tests)

c0_min = 2
c0_max = 11
c1_min = 2
c1_max = 11
k_rough = 1
pp_max = 1000 # max pseudoprimes

generate_spp_heatmap(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max)
generate_npp_heatmap(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max)

# Fermat case
n_values = list(range(1, 50))
c0_values = [-n**2 for n in n_values]
c1_values = [2 * n for n in n_values]

plt.plot(c0_values, c1_values, marker='o', linestyle='-', color='red', label='Fermat Case')

plot_spp_largerscale(c0_min, c0_max, c1_min, c1_max, 1, 1000)


#analyze_primality_test(lambda n: lucas_type_primality_test(n, 1, 2), "Lucas-Type Primality Test",1)
