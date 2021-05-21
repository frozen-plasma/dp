from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: [[int]]) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        print(envelopes)
        sols = []
        for env in envelopes:
            w, h = env[0], env[1]
            idx = bisect_left(sols, env[1])
            if idx == len(sols):
                sols.append(env[1])
            else:
                sols[idx] = env[1]
        return len(sols)

# 453-522, 29 minutes. solution using special lambda sort and LIS binary search algorithm using bisect left. O(nlogn)