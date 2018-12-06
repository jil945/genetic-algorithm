import random


def random_mutation(child, gene):
    for i in range(len(child)):
        child[i] = random.choice(gene)


def mutate_one(child, gene):
    index = random.randint(0, len(child) - 1)
    child[index] = random.choice(gene)


if __name__ == '__main__':
    child1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    genes = [i for i in range(100)]
    random_mutation(child1, genes)
    print(child1)
