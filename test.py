import json
import numpy as np
from problem import INITIAL_POPULATION, knapsack
from GA import genetic_algorithm
from selection import selection_elite, selection_best_half, selection_random_choice
from breeding import breeding_by_prob, breeding_by_splice, breeding_by_random_splice
from mutation import mutation_invert_bits, mutation_flip_k_bits, mutation_flip_uniform_bits


def save_result_csv(file_name, res_list):
    trials = len(res_list)
    data_list = []
    data = ["Generation"] + ["Average", "Standard Deviation", "Max", "Min", ""] * trials
    data_list.append(data)
    data = [""]
    for i in range(trials):
        data = data + ["Trail {0}".format(i + 1), "", "", "", ""]

    for g in range(len(res_list[0]["result"])):
        data = [g]
        for t in range(trials):
            r = res_list[t]["result"][g]
            data.append(r["average"])
            data.append(r["standardDeviation"])
            data.append(r["bestScore"])
            data.append(r["worstScore"])
            data.append("")
        data_list.append(data)
    
    print("Saving to...", file_name + ".csv")
    np.savetxt(file_name + ".csv", data_list, delimiter=',', fmt='%s')

def save_final_result_csv(file_name, res_list):
    data_list = [
        ["Trails", "Average", "Standard Deviation", "Max", "Min"]
    ]
    for t in range(len(res_list)):
        r = res_list[t]["final_result"]
        data_list.append([
            t + 1,
            r["average"],
            r["standardDeviation"],
            r["bestScore"],
            r["worstScore"]
        ])
    print("Saving to...", file_name + "(final).csv")
    np.savetxt(file_name + "(final).csv", data_list, delimiter=',', fmt='%s')

def knapsack_test_run(selection, breeding, mutation, trials=10):
    print(selection.__name__, breeding.__name__, mutation.__name__)

    res_list = []
    params = {
        "target_pop_num": len(INITIAL_POPULATION),
        "max_generations": 500
    }

    for i in range(trials):
        res = genetic_algorithm(knapsack, INITIAL_POPULATION, selection, breeding, mutation, **params)
        res_list.append({
            "trial": i + 1,
            "result": res,
            "final_result": res[-1]
        })

    file_name = "{0}-{1}-{2}".format(selection.__name__, breeding.__name__, mutation.__name__)
    print("Saving to...", file_name + ".json")
    with open(file_name + ".json", "w", encoding="utf-8") as f:
        json.dump(res_list, f)

    save_result_csv(file_name, res_list)
    save_final_result_csv(file_name, res_list)

def noop(fitness, population, **kargs):
    return population

def build_fn_list():
    res = []
    s_list = [noop, selection_elite, selection_best_half, selection_random_choice]
    b_list = [breeding_by_prob, breeding_by_splice, breeding_by_random_splice]
    m_list = [noop, mutation_invert_bits, mutation_flip_k_bits, mutation_flip_uniform_bits]
    for s in s_list:
        for b in b_list:
            for m in m_list:
                res.append((s, b, m))
    return res

if __name__ == "__main__":
    fn_list = build_fn_list()
    start = 4
    for i in range(start, len(fn_list)):
        s, b, m = fn_list[i]
        knapsack_test_run(s, b, m)
