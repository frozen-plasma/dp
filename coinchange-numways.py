'''
Given a value <amt>, if we want to make change for <amt> cents, and we have infinite supply of each of
<coins> = { S1, S2, .. , S<n>} valued coins, how many ways can we make the change?
'''
def coinchange(coins, n, amt):
    table = [[0 for j in range(n)] for i in range(amt+1)]

    for i in range(n):
        table[0][i] = 1

    for i in range(1, amt+1):
        for j in range(n):
            a = table[i-coins[j]][j] if i-coins[j] >= 0 else 0
            b = table[i][j-1] if j >= 1 else 0
            table[i][j] = a + b
    print(table)
    return table[amt][n-1]

arr = [1,5,7]
n = len(arr)
amt = 11
print(coinchange(arr, n, amt))