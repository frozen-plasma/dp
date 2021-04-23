def nc(n):
    sols = [-1]*(n+1)
    sols[1] = 1
    sols[2] = 1
    for i in range(3, n+1):
        if sols[i] == -1:
            sols[i] = sols[sols[i-1]] + sols[i-sols[i-1]]

    print(sols)
    return sols[-1]


print(nc(300))

print("test")