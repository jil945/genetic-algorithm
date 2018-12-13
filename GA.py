import math
import random
import time

def _calc_population(population, fitness) -> {}:
    best_child = None
    best_score = None
    worst_child = None
    worst_score = None
    sum_score = 0.0
    n = len(population)

    pop_score = [ fitness(p) for p in population ]

    for i, score in enumerate(pop_score):
        sum_score += score

        if best_score is None or score > best_score:
            best_score = score
            best_child = population[i]
        if worst_score is None or score < worst_score:
            worst_score = score
            worst_child = population[i]

    avg = sum_score / n
    var = 0
    for score in pop_score:
        var += (score - avg) ** 2
    var = var / (n - 1)

    std = math.sqrt(var)

    return {
        "bestScore": best_score,
        "bestChild": best_child,
        "worstScore": worst_score,
        "worstChild": worst_child,
        "average": avg,
        "variance": var,
        "standardDeviation": std,
        "population": population,
        "fitness": pop_score
    }
def genetic_algorithm(fitness, initial, selection, breeding, mutation, target_score=None, max_generations=100, *args, **kargs):
    """Run the genetic algorithm based on the provided selection, breeding, mutation function
    
    Args:
        fitness (None): Fitness function, takes in member of population, returns flaot
        initial ([None]): initial population
        selection (None): selection step, takes in fitness, population, *args, **kargs, returns population
        breeding (None): breeding step, takes in fitness, population, *args, **kargs, returns population
        mutation (None): mutation step, takes in fitness, population, *args, **kargs, returns population
        target_score (float, optional): Defaults to None. target score for fitness function to reach
        max_generations (int, optional): Defaults to 100. Max iterations the loop will run for
    
    Returns:
        [None]: Result list
    """
    res_list = []
    pop = initial
    result = _calc_population(pop, fitness)
    score = result["bestScore"]
    # child = result["bestChild"]
    res_list.append(result)
    i = 1
    def check_stop():
        one = False
        if target_score is not None:
            one = (score >= target_score)
        two = (i >= max_generations)
        return one or two

    
    while not check_stop():

        start = time.time()
        pop = selection(fitness, pop, *args, **kargs)
        pop = breeding(fitness, pop, *args, **kargs)
        pop = mutation(fitness, pop, *args, **kargs)
        end = time.time()

        result = _calc_population(pop, fitness)
        result["time"] = end - start
        score = result["bestScore"]
        # child = result["bestChild"]
        res_list.append(result)
        i += 1
    return res_list

if __name__ == "__main__":
    # Sample setup
    # DO NOT ACTUALLY USE IT

    def _generate_word(length, begin, step):
        return "".join([ chr(random.randint(begin, begin + step - 1)) for _ in range(length) ])

    def initial_pop(sizePop, lengthOfChild, begin, step):
        return [ _generate_word(lengthOfChild, begin, step) for _ in range(sizePop) ]

    def selection_fn(fitness, population, best, lucky, **kargs):
        scored_pop = [ (fitness(p), p) for p in population ]
        scored_pop.sort(key=lambda x: x[0], reverse=True)

        next_pop = [ p for _, p in scored_pop[:best] ]
        end = len(scored_pop) - 1

        for _ in range(lucky):
            i = random.randint(best, end)
            next_pop.append(scored_pop[i][1])

        random.shuffle(next_pop)
        return next_pop

    def _create_child(parent1: str, parent2: str) -> str:
        child = ""
        for i in range(len(parent1)):
            prob = 100 * random.random()
            if prob < 50:
                child += parent1[i]
            else:
                child += parent2[i]
        return child
    
    def breeding_fn(fitness, population, num_of_children, **kargs):
        next_pop = []
        l = len(population)
        for i in range(l // 2):
            for _ in range(num_of_children):
                next_pop.append(_create_child(population[i], population[l - i - 1]))
        return next_pop

    def _mutate(word, begin, step):
        i = int(random.random() * len(word))
        word[i] = chr(random.randint(begin, begin + step - 1))
        return word

    def mutation_fn(fitness, population, chance_of_mutation, begin, step, **kargs):
        for i in range(len(population)):
            prob = random.random() + 100
            if prob < chance_of_mutation:
                population[i] = _mutate(population[i], begin, step)
        return population

    password = "helloworld"
    def f(word):
        if len(word) != len(password):
            return 0.0
        else:
            score = 0
            for i, p in enumerate(password):
                if p == word[i]:
                    score += 1
            return score * 100 / len(password)

    params = {
        "begin": 97,
        "step": 26,
        "best": 30,
        "lucky": 20,
        "num_of_children": 4,
        "chance_of_mutation": 50,
        "target_score": 100.0,
        "max_generations": 100
    }
    pop = initial_pop(100, len(password), params["begin"], params["step"])
    res = genetic_algorithm(f, pop, selection_fn, breeding_fn, mutation_fn, **params)
    print(res)
    pass