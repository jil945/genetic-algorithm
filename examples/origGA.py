import numpy as np
import random

"""
Genetic Algorithm based on https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9
"""

def _fitness(password: str, test_word: str) -> float:
    if len(test_word) != len(password):
        return 0.0
    else:
        score = 0
        for i, p in enumerate(password):
            if p == test_word[i]:
                score += 1
        return score * 100 / len(password)

def _generateWord(length: int, begin=97, step=26) -> str:
    return "".join([ chr(random.randint(begin, begin + step - 1)) for _ in range(length) ])

def _generateFirstPopulation(sizePop: int, password: str) -> [str]:
    l = len(password)
    return [ _generateWord(l) for _ in range(sizePop) ]

def _getBestChild(population: [str], password: str, fitness=_fitness) -> (float, str):
    score = None
    child = None

    for p in population:
        s = fitness(password, p)
        if score is None or s > score:
            score = s
            child = p
    return score, child

def _selectFromPopulation(population: [str], password: str, best: int, lucky: int, fitness=_fitness) -> [str]:
    scoredPop = [ (fitness(password, p), p) for p in population ]
    scoredPop.sort(key=lambda x: x[0], reverse=True)

    nextPop = [ p for _, p in scoredPop[:best] ]
    end = len(scoredPop) - 1

    for _ in range(lucky):
        i = random.randint(best, end)
        nextPop.append(scoredPop[i][1])

    return nextPop

def _createChild(parent1: str, parent2: str) -> str:
    child = ""
    for i in range(len(parent1)):
        prob = 100 * random.random()
        if prob < 50:
            child += parent1[i]
        else:
            child += parent2[i]
    return child
def _createChildren(breeders: [str], numOfChild: int) -> [str]:
    nextPop = []
    l = len(breeders)
    for i in range(l // 2):
        for _ in range(numOfChild):
            nextPop.append(_createChild(breeders[i], breeders[l - i - 1]))
    return nextPop

def _mutate(word: str, begin=97, step=26) -> str:
    i = int(random.random() * len(word))
    word[i] = chr(random.randint(begin, begin + step - 1))
    return word

def _mutatePopulation(population: [str], chanceOfMutate=50) -> [str]:
    for i in range(len(population)):
        prop = random.random() + 100
        if prop < chanceOfMutate:
            population[i] = _mutate(population[i])
    return population


def geneticAlgorithm(password: str, begin=97, step=26, populationSize=100, fitness=_fitness, targetScore=100.0, maxGenerations=100):
    pop = _generateFirstPopulation(populationSize, password)

    score, child = _getBestChild(pop, password, fitness=fitness)
    i = 1
    while score < targetScore and i < maxGenerations:
        print(score, child)
        pop = _selectFromPopulation(pop, password, best=30, lucky=20, fitness=fitness)
        pop = _createChildren(pop, 4)
        pop = _mutatePopulation(pop)
        score, child = _getBestChild(pop, password, fitness=fitness)
        i += 1
    
    return child

if __name__ == "__main__":

    def fit(password, test_word):
        score = 0.0
        for t in test_word:
            if t == "a":
                score += 1
        return score

    c = geneticAlgorithm("123456", fitness=fit, targetScore=6)
    print(c)
    pass