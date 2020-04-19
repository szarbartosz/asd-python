def knapsack_problem(weight, profit, max_weight):
    n = len(weight)
    F = [None] * n
    for i in range(n):
        F[i] = [0] * (max_weight + 1)
    for i in range(weight[0], max_weight + 1):
        F[0][i] = profit[0]
    for i in range(1, n):
        for j in range(1, max_weight + 1):
            F[i][j] = F[i - 1][j]
            if j >= weight[i]:
                F[i][j] = max(F[i][j], F[i - 1][j - weight[i]] + profit[i])
    return F[n - 1][max_weight]


weight = [4,1,2,4,3,5,10,3]
profit = [7,3,2,10,4,1,7,2]
print(knapsack_problem(weight, profit, 10))


def knapsack(W, P, max_w):
    n = len(P)
    F = [None] * n
    for i in range(n):
        F[i] = [0] * (max_w + 1)
    for w in range(W[0], max_w + 1):
        F[0][w] = P[0]
    for i in range(1, n):
        for w in range(1, max_w + 1):
            F[i][w] = F[i - 1][w]
            if W[i] <= w:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    return F[n - 1][max_w]


W = [4,1,2,4,3,5,10,3]
P = [7,3,2,10,4,1,7,2]
print(knapsack_problem(W, P, 10))