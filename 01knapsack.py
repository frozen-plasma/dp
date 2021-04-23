def knapsack(cap, weights, values, n):
    mat = [[-1 for j in range(cap+1)] for i in range(n+1)]

    for i in range(n+1): #represents the current item considered in the knapsack
        for j in range(cap+1): #represents the current capacity available
            print("i: ", i, "weight from weights[i-1]: ", weights[i-1], "and j: ", j)
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif j >= weights[i-1]: #if you have enough weight to carry the current item:
                print("if weights[i-1] (", weights[i-1], ") <= j (", j, "), \n mat[i][j] = max(values[i-1] + mat[i-1][j-weights[i-1]], mat[i-1][j]")
                print("max of: (", values[i-1], " + ", mat[i-1][j-weights[i-1]], ", ", mat[i-1][j], ")")
                mat[i][j] = max(values[i-1] + mat[i-1][j-weights[i-1]], mat[i-1][j])
                #current max value is equal to the max value from (current item n's value + maximal value of the
                # item(s) (n-1...1) that can be carried at the current weight j minus weight of the current
                # item considered, maximal value of the previous items(n-1...1) at the current weight j
            else: #current carry weight is too low to carry the current item. carrying the previous selection of items
                  #that give the maximum weight at this carry weight instead.
                print("setting current max value to previous items (n-1...1) at the current weight j: ", mat[i-1][j])
                mat[i][j] = mat[i-1][j]
                #else current max value is equal to max value of the previous items (n-1...1) at the current weight j
            print(mat, "\n")
    return mat[n][cap]

values = [10, 15, 40]
weights = [1, 2, 3]
cap = 6
n = 3
print(knapsack(cap, weights, values, n))
#print(knapsack(cap, weights, values, n))
