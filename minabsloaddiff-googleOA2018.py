'''
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Example 1:

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.
'''

#so across is current load/capacity, down is current job

def loadbalancer(A):
    cap = sum(A)//2
    sols = [[-1 for j in range(cap+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                sols[i][j] = 0
            elif j >= A[i-1]:
                sols[i][j] = max(A[i-1] + sols[i-1][j-A[i-1]], sols[i-1][j])
            else:
                sols[i][j] = sols[i-1][j]
            print(sols)
    print(cap)
    power = sols[-1][-1]
    powerr = abs(sum(A)-(power*2))
    return powerr





A = [1,2,3,4,5]
A2 = [3,1,3,5,7]
A3 = [1,1,1,1,1,1,1,4,3]

print(loadbalancer(A2))