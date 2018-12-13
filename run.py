from selection import selection_elite
from breeding import breeding_by_prob
from mutation import mutation_flip_uniform_bits
from GA import genetic_algorithm
from problem import knapsack, INITIAL_POPULATION

if __name__ == "__main__":
    params = {
        "target_pop_num": len(INITIAL_POPULATION),
        "max_generations": 500
    }
    res = genetic_algorithm(knapsack, INITIAL_POPULATION, selection_elite, breeding_by_prob, mutation_flip_uniform_bits, **params)
    print(res[-1])