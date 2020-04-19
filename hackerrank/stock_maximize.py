def stockmax(prices):
    n = len(prices)
    max_price = 0
    profit = 0
    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        profit += max_price - prices[i]
    return profit


prices = [1,2,100]
print(stockmax(prices))