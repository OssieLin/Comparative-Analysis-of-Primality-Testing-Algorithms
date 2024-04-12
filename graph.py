import seaborn as sns
from primality_test import *


def plot_combined_graph_from_tests(primality_tests):
    colors = ['red', 'sandybrown', 'royalblue']  # Define colors for each test
    counters = []

    for i, (primality_test, test_name, k) in enumerate(primality_tests):
        counter = PseudoprimeCounter(primality_test, test_name, k)
        counter.count_pseudoprimes(k)
        counters.append(counter)

        x_values = range(2, 2 + len(counter.accumulated_pseudoprime_values))
        plt.plot(x_values, counter.accumulated_pseudoprime_values, marker='o', label=test_name, color=colors[i])

    plt.title('Number of 3-rough Pseudoprimes up to N')
    plt.xlabel('N')
    plt.ylabel('Number of Pseudoprimes')
    plt.grid(True)
    plt.legend()
    plt.show()

def generate_spp_heatmap(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max):
    list_of_spp = [[smallest_lucas_type_pseudoprime(c0, c1, k_rough, pp_max) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)[::-1]]

    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=range(c0_min, c0_max), yticklabels=range(c1_min, c1_max)[::-1])
    plt.title('Logs of Smallest 3-rough Pseudoprimes ', fontdict={'fontsize':13})
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()

def generate_npp_heatmap(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max):
    list_of_spp = [[number_of_lucas_type_pseudoprime_up_to(c0, c1, k_rough, pp_max) for c0 in range(c0_min, c0_max)] for c1 in range(c1_min, c1_max)[::-1]]

    sns.heatmap(list_of_spp, cmap="YlGnBu", annot=True, fmt="d", xticklabels=range(c0_min, c0_max), yticklabels=range(c1_min, c1_max)[::-1])
    plt.title(f'Number of 3-rough Pseudoprimes up to 1000', fontdict={'fontsize': 13})
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.show()

def plot_spp_largerscale(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max):
    list_of_spp = [[log_of_smallest_lucas_type_pseudoprime_k_rough(c0, c1, k_rough, pp_max) for c0 in range(c0_min, c0_max)] for c1
                      in range(c1_min, c1_max)]

    plt.imshow(list_of_spp, extent=(c0_min, c0_max, c1_min, c1_max))  #
    plt.title('Logs of Smallest Pseudoprimes')
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.xticks(range(c0_min, c0_max, 20))
    plt.yticks(range(c1_min, c1_max, 20))
    plt.colorbar()
    plt.show()


def plot_heatmap_lucastype_nrpseudoprimes(c0_min, c0_max, c1_min, c1_max, k_rough, pp_max):
    data = [[number_of_lucas_type_pseudoprime_up_to(c0, c1, k_rough, pp_max) for c0 in range(c0_min, c0_max + 1)] for c1 in range(c1_min, c1_max + 1)]

    plt.imshow(data, cmap='viridis', origin='lower', extent=[c0_min, c0_max, c1_min, c1_max])
    plt.colorbar()
    plt.title('Number of Lucas-Type Pseudoprimes up to ' + str(pp_max) + " with 2_rough")
    plt.xlabel('Parameter c0')
    plt.ylabel('Parameter c1')
    plt.xticks(range(c0_min, c0_max + 1, 10))
    plt.yticks(range(c1_min, c1_max + 1, 10))
    plt.show()

