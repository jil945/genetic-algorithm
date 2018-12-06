import random
import selection as select
import breeding as breed
import mutation as mutate

print("yup")
def genetic_algorithm(population, genes, fitness_func, select_func, cross_func, mutate_func, max_generations=200):
    perfect_fit = False
    generation = 0
    pop = []
    for _ in range(population):
        child = create_chromosome(genes)
        pop.append(child)

    while not perfect_fit and generation < max_generations:
        pop = sorted(pop, key=lambda x: fitness_func(x))
        if fitness_func(pop[0]) == 0:
            perfect_fit = True
        else:
            new_pop = []
            new_pop.extend(select_func(pop, population))  # Selection
            remaining_pop_num = population - len(new_pop)
            for _ in range(remaining_pop_num):
                parent1 = random.choice(new_pop)
                parent2 = random.choice(new_pop)
                child = cross_func(parent1, parent2)
                mutate_func(child, genes)
                new_pop.append(child)
            pop = new_pop[:]

            # print("Generation: {}, Best Offspring: {}".format(generation + 1, "".join(pop[0])))
            generation += 1

    print("Generation: {}, Best Offspring: {}".format(generation + 1, "".join(pop[0])))


def create_chromosome(genes):
    target = "Yo dawg"
    chromosome = [random.choice(genes) for _ in range(len(target))]
    return chromosome


def fitness(chromosome):
    fit_score = 0
    target = "Yo dawg"
    for chd, optimal in zip(chromosome, target):
        if chd != optimal:
            fit_score += 1
    return fit_score


if __name__ == "__main__":
    gene_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

    print("1, 1, 1")  # 1, 1, 1
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_splice, mutate.mutate_one)
    print("\n1, 1, 2")  # 1, 1, 2
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_splice, mutate.random_mutation)

    print("\n1, 2, 1")  # 1, 2, 1
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_prob, mutate.mutate_one)
    print("\n1, 2, 2")  # 1, 2, 2
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_prob, mutate.random_mutation)

    print("\n1, 3, 1")  # 1, 3, 1
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_random, mutate.mutate_one)
    print("\n1, 3, 2")  # 1, 3, 2
    genetic_algorithm(100, gene_pool, fitness, select.elite_selection, breed.breed_by_random, mutate.random_mutation)

    print("\n2, 1, 1")  # 2, 1, 1
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_splice, mutate.mutate_one)
    print("\n2, 1, 2")  # 2, 1, 2
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_splice, mutate.random_mutation)

    print("\n2, 2, 1")  # 2, 2, 1
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_prob, mutate.mutate_one)
    print("\n2, 2, 2")  # 2, 2, 2
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_prob, mutate.random_mutation)

    print("\n2, 3, 1")  # 2, 3, 1
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_random, mutate.mutate_one)
    print("\n2, 3, 2")  # 2, 3, 2
    genetic_algorithm(100, gene_pool, fitness, select.best_half_selection, breed.breed_by_random, mutate.random_mutation)

    print("\n3, 1, 1")  # 3, 1, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_splice, mutate.mutate_one)
    print("\n3, 1, 2")  # 3, 1, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_splice, mutate.random_mutation)

    print("\n3, 2, 1")  # 3, 2, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_prob, mutate.mutate_one)
    print("\n3, 2, 2")  # 3, 2, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_prob, mutate.random_mutation)

    print("\n3, 3, 1")  # 3, 3, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_random, mutate.mutate_one)
    print("\n3, 3, 2")  # 3, 3, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_kth_selection, breed.breed_by_random, mutate.random_mutation)

    print("\n4, 1, 1")  # 4, 1, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_splice, mutate.mutate_one)
    print("\n4, 1, 2")  # 4, 1, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_splice, mutate.random_mutation)

    print("\n4, 2, 1")  # 4, 2, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_prob, mutate.mutate_one)
    print("\n4, 2, 2")  # 4, 2, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_prob, mutate.random_mutation)

    print("\n4, 3, 1")  # 4, 3, 1
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_random, mutate.mutate_one)
    print("\n4, 3, 2")  # 4, 3, 2
    genetic_algorithm(100, gene_pool, fitness, select.random_choice_selection, breed.breed_by_random, mutate.random_mutation)
