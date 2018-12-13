import random

def random_mutation(fitness, population, begin, step):
    for i in range(len(population)):
        temp = ""
        for j in range(len(population[i])):
            temp = temp + chr(random.randint(begin, begin + step - 1))
        population[i] = temp[:]
    return population


def mutate_one(fitness, population, begin, step):
    for j in range(len(population)):
        i = int(random.randint(0, len(population[j])))
        temp = population[j][:i] + chr(random.randint(begin, begin + step - 1)) + population[j][(i + 1):]
        # above is faster than turning strings into lists of chars and back to strings
        population[j] = temp[:]
    return population

def flip_bit_k_random_each(fitness, population):
    """
    Flips K random bits in rounds
    Ex. [1, 0, 1] flips K random bits in 30 or less rounds
    [1, 0] flips K random bits in 20 or less rounds
    etc.
    """
    for bits in population:
        rounds = random.randint(0, len(bits)*10)
        count = 0
        while count < rounds:
            select_number = random.randint(0, len(bits) - 1)
            bits[select_number] = (bits[select_number] + 1) % 2
            count += 1
    return population

def _flip_all_bits(bits):
    for i in range(len(bits)):
        bits[i] = (bits[i] + 1) % 2
    return bits

def mutation_invert_bits(fitness, population, chance_of_mutate=0.5, **kargs):
    for i in range(len(population)):
        if random.random() < chance_of_mutate:
            population[i] = _flip_all_bits(population[i])
    return population

def _flip_k_bits(bits, k):
    flipped = set()
    for _ in range(k):
        s = random.randint(0, len(bits) - 1)
        # ensures each bit is only flipped once
        while s in flipped:
            s = random.randint(0, len(bits) - 1)
        flipped.add(s)

        bits[s] = (bits[s] + 1) % 2
    return bits

def mutation_flip_k_bits(fitness, population, k_bits=None, chance_of_mutate=0.5, **kargs):
    k = len(population[0]) // 2 if k_bits is None else k_bits

    for i in range(len(population)):
        if random.random() < chance_of_mutate:
            population[i] = _flip_k_bits(population[i], k)
    return population

# Worse version of uniform
def mutation_flip_one_bit(fitness, population, chance_of_mutate=0.5, **kargs):
    for i in range(len(population)):
        if random.random() < chance_of_mutate:
            population[i] = _flip_k_bits(population[i], 1)
    return population

def _flip_uniform_bits(bits):
    chance_to_flip = 1 / len(bits)
    for i in range(len(bits)):
        if random.random() < chance_to_flip:
            bits[i] = (bits[i] + 1) % 2
    return bits

def mutation_flip_uniform_bits(fitness, population, chance_of_mutate=0.5, **kargs):
    for i in range(len(population)):
        if random.random() < chance_of_mutate:
            population[i] = _flip_uniform_bits(population[i])
    return population


if __name__ == '__main__':
    from copy import deepcopy

    def _generateWord(length, begin, step):
        return "".join([chr(random.randint(begin, begin + step - 1)) for _ in range(length)])

    def initialPop(sizePop, lengthOfChild, begin, step):
        return [_generateWord(lengthOfChild, begin, step) for _ in range(sizePop)]

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


    print(random_mutation(f, initialPop(10, len(password), 97, 26), 97, 26))
    print(mutate_one(f, initialPop(10, len(password), 97, 26), 97, 26))

    # Testing bit mutations
    pop = [ [random.randint(0, 1) for _ in range(10) ] for _ in range(10) ]
    print(mutation_invert_bits(f, deepcopy(pop)))
    print(mutation_flip_k_bits(f, deepcopy(pop)))
    print(mutation_flip_one_bit(f, deepcopy(pop)))
    print(mutation_flip_uniform_bits(f, deepcopy(pop)))

    """
    child1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    genes = [i for i in range(100)]
    random_mutation(child1, genes)
    print(child1)
    """
