import numpy as np
from itertools import permutations

data = np.genfromtxt("model_forecasts.txt", delimiter=',')


def find_optimal_pairs(matrix):
    teams = np.arange(10) 
    best_score = np.inf
    best_combination = None

    for pairs in permutations(teams, 10):  
        pairs = np.array(pairs).reshape(2, 5) 
        score = sum(matrix[pairs[0, i], pairs[1, i]]**2 for i in range(5))
        
        if score < best_score:
            best_score = score
            best_combination = pairs

    return best_combination

optimal_pairs = find_optimal_pairs(data)
print(optimal_pairs)
