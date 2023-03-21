prices = [7,1,5,3,6,4]

def profit(prices):
    profits = []

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[i] - prices[j]
            profits.append(profit)

    return max(profits)

print(profit(prices = prices))