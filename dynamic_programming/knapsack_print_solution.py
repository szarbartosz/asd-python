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
    return F


def solution(weight, profit, max_weight, items):
    arr = knapsack_problem(weight, profit, max_weight)
    n = len(weight)
    result = arr[n - 1][max_weight]
    for i in range(n - 1, -1, -1):
        if result <= 0:
            break
        if result == arr[i - 1][max_weight]:
            continue
        else:
            items.append(i)
            result -= profit[i]
            max_weight -= weight[i]
    return items


weight = [4,1,2,4,3,5,10,3]
profit = [7,3,2,10,4,1,7,2]
max_weight = 10
items = []
print('indexes of chosen items: ', solution(weight, profit, max_weight, items))