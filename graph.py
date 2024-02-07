import seaborn as sns
from primality_test import *
from util import *

def plot_combined_graph_from_tests(primality_tests):
    counters = []
    for primality_test, test_name, k in primality_tests:
        counter = PseudoprimeCounter(primality_test, test_name,k)
        counter.count_pseudoprimes(k)
        counters.append(counter)

    for counter in counters:
        x_values = range(2, 2 + len(counter.accumulated_pseudoprime_values))
        plt.plot(x_values, counter.accumulated_pseudoprime_values, marker='o', label=counter.primality_test_name)

    plt.title('Number of Pseudoprimes vs Numerical Value Comparison')
    plt.xlabel('Numerical Value')
    plt.ylabel('Number of Pseudoprimes')
    plt.grid(True)
    plt.legend()
    plt.show()


def generate_pseudoprime_heatmap(c0_range, c1_range):
    list_of_spp = [[smallest_lucas_type_pseudoprime(c0, c1) for c0 in c0_range] for c1 in c1_range]
    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=c0_range, yticklabels=c1_range)
    plt.title('Smallest Pseudoprimes Heatmap of Lucas-Type Sequence')
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()

def generate_pseudoprime_heatmap_up_to(c0_range, c1_range):
    list_of_spp = [[smallest_lucas_type_pseudoprime_up_to(c0, c1) for c0 in c0_range] for c1 in c1_range]
    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=c0_range, yticklabels=c1_range)
    plt.title('Numbers of Pseudoprimes Heatmap of Lucas-Type Sequence up to 1000', fontdict={'fontsize': 10})
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()

def plot_heatmap_lucastype_nrpseudoprimes(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max):
    data = [[lucas_type_primality_test(n, c0, c1) and is_k_pseudoprime(n, k_rough)
             for n in range(3, pp_max + 1)]
            for c0 in range(c0_min, c0_max + 1)
            for c1 in range(c1_min, c1_max + 1)]

    plt.imshow(data, cmap='viridis', origin='lower', extent=[c0_min, c0_max, c1_min, c1_max])
    plt.colorbar()
    plt.title('Number of Lucas-Type Pseudoprimes')
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()
