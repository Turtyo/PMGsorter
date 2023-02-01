import json
from math import exp
import numpy as np
import numpy.typing as npt
import pulp
from typing import NewType
import padding


Pulp_Lp_Problem = NewType("Pulp_Lp_Problem", pulp.pulp.LpProblem)
Ranking_matrix = list[list[int]]
Activities_matrix = npt.NDArray[npt.NDArray[int]]
Weight_matrix = npt.NDArray[npt.NDArray[int]]

def decode_json() -> tuple[int, int]:
    with open("./values.json", "r") as f:
        content = f.read()
        values = json.loads(content)
    return values["Vmax"], values["lambda"]


def sort_ranking_by_activities(ranking: Ranking_matrix, m: int) -> Activities_matrix:
    """
    Sorts the rankings of each subject to make it so that each column represents an activity, and not the ranking given by each subject to an activity
    A list like [1,3,4,2] which means that the subject wants the activity 1, then 3, then 4, then 2 will thus become [1,4,2,3] (activity 1 is ranked 1st, activity 2 is ranked 4th...)
    m -> int : number of activities that each subject should classify, needed since we can't be sure any of the subjects has ranked the correct number

    return : numpy array, ranking ordered by activity
    """
    n = len(ranking)  # number of lines which is the number of subjects
    ranking_ordered = np.zeros((n, m))
    for i in range(n):
        for j in range(len(ranking[i])):
            ranking_ordered[i, ranking[i][j] - 1] = j + 1
    return ranking_ordered


def create_weight_matrix(ranking_ordered: Activities_matrix) -> Weight_matrix:
    """
    ranking_ordered : matrix where lines are subjects and each column represents an activity, which means ranking_ordered[i,j] is the ranking given by subject i
    to activity j (from 1 to m)

    return: a weight matrix
    """
    n, m = ranking_ordered.shape
    w = np.zeros((n, m))
    _Vmax, _lambda = decode_json()
    for i in range(n):
        for j in range(m):
            w[i, j] = round(_Vmax * exp(-ranking_ordered[i, j] * _lambda))
    return w

def formate_matrix(ranking: Ranking_matrix, m : int, padding_name: str = "random") -> Weight_matrix:
    """
    This function will transform the classification we get from the subject into a matrix that is usable by the model, by applying the functions defined above and in padding
    m : number of activities that each subject should classify
    """
    ranking_ordered = sort_ranking_by_activities(ranking, m)
    weight_matrix = create_weight_matrix(ranking_ordered)
    return padding.pad_matrix(weight_matrix,padding_name=padding_name)


def solve_problem(n: int, m: int, p: int, k: int, w: int) -> Pulp_Lp_Problem:
    # We define a new problem
    prob = pulp.LpProblem("Assignment", pulp.LpMaximize)

    ## Constraints
    # Each subject must have k activities
    global a
    for i in range(n):
        prob += pulp.lpSum(a[i, :]) == k

    # Not more subject by activity than the maximum number allowed
    for j in range(m):
        prob += pulp.lpSum(a[:, j]) <= p[j]

    # Objective function
    prob += pulp.lpSum(w * a)

    # Problem solving
    status = prob.solve()

    # Optimum values
    print("Status: ", pulp.LpStatus[status], "\n")

    # We make sure the problem can be solved
    assert pulp.LpStatus[prob.solve()] == "Optimal"
    return prob


### TEST PART

if __name__ == "__main__":

    ### INPUT
    ranking = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [2, 1, 3]]

    # number of places in each activity
    p = [2, 1, 1]

    # k activities must be affected to each subject
    k = 1

    # n is the number of subject, m the number of activities
    m = len(p)
    n = len(ranking)

    # Weight matrix (or matrix of preferences)
    sorted_by_activities = sort_ranking_by_activities(ranking, m)
    w = create_weight_matrix(sorted_by_activities)

    print(np.array(w))

    ###
    ### PRELIMINARY CHECK
    # Asserting there are enough places for everyone
    assert sum(p) >= n * k
    assert len(p) == m

    ###
    ### SOLVE
    # Decision variables
    a = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            a[i, j] = pulp.LpVariable(f"a_{i}_{j}", cat=pulp.LpBinary)

    prob = solve_problem(n, m, p, k, w)
    ###
    ### DISPLAY RESULTS

    A = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(pulp.value(a[i, j]))
        A.append(line)

    print("Variables:")
    print(np.array(A))

    print("Objective: ", pulp.value(prob.objective))
    ###

    ### Sorting tests
    



    ranking_bis = [ [1, 2, 3],
                    [1],
                    [3, 1],
                    [2, 3, 1]]
    
    rk_ord = sort_ranking_by_activities(ranking_bis,3)
    #should return [[1. 2. 3.]
    #               [1. 0. 0.]
    #               [2. 0. 1.]
    #               [3. 1. 2.]]
    # for line 4 for example [2,3,1] means activity 2 is 1st choice, activity 3 is 2nd choice and activity 1 is 3rd choice, which gives [3,1,2] when each column is an activity


    print("\nRanking bis : ")
    print(ranking_bis)
    print("\nRanking ordered :")
    print(rk_ord)

