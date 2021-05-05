#first pass
def maxProfit(self, prices: [int]) -> int:
    if (len(prices) == 1):
        return 0
    print(prices)
    profit = 0
    low = prices[0]
    high = prices[1]
    if (len(prices) == 2):
        profit = high - low
    for i in range(2, len(prices)):
        clow = prices[i - 1]
        chigh = prices[i]
        if (clow < low):
            low = clow
            high = 0
        if (chigh > high):
            high = chigh
        print(high, low)
        if ((high - low) > profit):
            profit = high - low
    if (profit < 0):
        return 0
    else:
        return profit

#second pass
def maxProfit2(self, prices: [int]) -> int:
    if len(prices) == 1:
        return 0
    prof = 0
    low = prices[0]
    sols = [0]
    for i in range(1, len(prices)):
        if prices[i] < low:
            low = prices[i]
        if prices[i] > low:
            sols.append(prices[i] - low)
    print(sols)
    return max(sols)

# 1157-1205 - new record, 8 minutes
