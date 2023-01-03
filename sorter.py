from math import exp
import numpy as np
import pulp

def create_weight_matrix(ranking, m):
    """
    ranking: matrix where lines are subjects and the 
    column represents the number associated to activity (1 to m)
    m: number of activities

    return: a weight matrix
    """
    w = []
    n, m = np.array(ranking).shape
    _Vmax = 10 # Arbitrary value for now
    _lambda = 1 # Arbitrary value for now
    for i in range(n):
        w_line = [0]*m
        for j in range(m):
            value = round(_Vmax*exp(-j*_lambda))
            w_line[ranking[i][j] - 1] = value
        w.append(w_line)
    return w

def solve_problem(n, m, p, k, w):
    # We define a new problem 
    prob = pulp.LpProblem("Assignment", pulp.LpMaximize)

    ## Constraints
    # Each subject must have k activities
    for i in range(n):
        prob += pulp.lpSum(a[i,:]) == k

    # Not more subject by activity than the maximum number allowed
    for j in range(m):
        prob += pulp.lpSum(a[:,j]) <= p[j]


    # Objective function
    prob += pulp.lpSum(w * a)

    # Problem solving
    status = prob.solve()

    # Optimum values
    print('Status: ',pulp.LpStatus[status],'\n')

    # We make sure the problem can be solved
    assert pulp.LpStatus[prob.solve()] == 'Optimal'
    return prob

### INPUT
ranking = [ [1, 2, 3],
            [1, 3, 2],
            [3, 1, 2]]
# n is the number of subject, m the number of activities
n,m = np.array(ranking).shape

# Weight matrix (or matrix of preferences)
w = create_weight_matrix(ranking, m)
print(np.array(w))

# number of places in each activity
p = [1, 1, 1]

# k subject must be affected to each subject
k = 1

###
### PRELIMINARY CHECK
# Asserting there are enough places for everyone
assert sum(p) >= n*k
assert len(p) == m
assert np.array(ranking).shape == np.array(w).shape

###
### SOLVE
# Decision variables
a = np.empty((n,m), dtype=object)
for i in range(n):
    for j in range(m):
        a[i,j] = pulp.LpVariable('a_{}_{}'.format(i,j),cat=pulp.LpBinary)

prob = solve_problem(n, m, p, k, w)
###
### DISPLAY RESULTS

A = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(pulp.value(a[i,j]))
    A.append(line)

print("Variables:")
print(np.array(A))

print('Objective: ', pulp.value(prob.objective))
###