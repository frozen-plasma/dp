def knapsack(cap, weights, values, n):
    mat = [[-1 for j in range(cap+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(cap+1):
            print("weight: ", weights[i-1], "and j: ", j)
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif weights[i-1] <= j:
                print("if weights[i-1] (", weights[i-1], ") <= j (", j, "), \n mat[i][j] = max(values[i-1] + mat[i-1][j-weights[i-1]], mat[i-1][j]")
                print("max of: (", values[i-1], " + ", mat[i-1][j-weights[i-1]], ", ", mat[i-1][j], ")")
                mat[i][j] = max(values[i-1] + mat[i-1][j-weights[i-1]], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
            print(mat, "\n")
    return mat[n][cap]

values = [40, 15, 10]
weights = [3, 2, 1]
cap = 6
n = 3
print(knapsack(cap, weights, values, n))
#print(knapsack(cap, weights, values, n))
