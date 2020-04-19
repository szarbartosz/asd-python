# Bartosz Szar
def knapsack(A, k):
    for i in range(len(A)):
        A[i] = (A[i][0], A[i][1], (A[i][0] / A[i][1])) #add profit/weight ratio to each tuple
    A.sort(key=lambda tup: tup[2], reverse=True) #sort descending by the profit/weight ratio
    profit = 0
    weight = k
    for i in range(len(A)):
        if A[i][1] <= weight:
            profit += A[i][0]
            weight -= A[i][1]
        else:
            profit += weight * A[i][2]
            return profit
    return profit


# elementarny test, powinien wypisać 12
A = [(1,1), (10,2), (6,3)]
print(knapsack(A, 3))

A = [(10,2)]
print(knapsack(A,0.5))