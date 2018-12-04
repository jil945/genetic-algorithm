import random


def elite_selection(children, pop_number):
    elite_candidates = []
    selection = int((.1 * pop_number))
    elite_candidates.extend(children[:selection])
    return elite_candidates


def best_half_selection(children, pop_number):
    best_half_candidates = []
    selection = int((.5 * pop_number))
    best_half_candidates.extend(children[:selection])
    return best_half_candidates


def random_selection(children, pop_number):
    random_candidates = []
    selection = int((.25 * pop_number))
    for _ in range(selection):
        random_candidates.append(random.choice(children))
    return random_candidates


if __name__ == "__main__":
    print("Yup")
