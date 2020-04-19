def memoized_knapsack(weight, profit, max_weight, n):
    if n == 0 or max_weight == 0:
        return 0
    if weight[n - 1] > max_weight:
        return memoized_knapsack(weight, profit, max_weight, n - 1)
    if memo[n - 1][max_weight] > 0:
        return memo[n - 1][max_weight]
    else:
        memo[n - 1][max_weight] = max(memoized_knapsack(weight, profit, max_weight, n - 1), memoized_knapsack(weight, profit, max_weight - weight[n - 1], n - 1) + profit[n - 1])
        return memo[n - 1][max_weight]



weight = [4,1,2,4,3,5,10,3]
profit = [7,3,2,10,4,1,7,2]
max_weight = 10
n = len(weight)
memo = [None] * n
for i in range(n):
    memo[i] = [-float('inf')] * (max_weight + 1)

print('solution:', memoized_knapsack(weight, profit, max_weight, n - 1))