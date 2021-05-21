#historical pass
class Solution1:
    def lengthOfLIS(self, nums: [int]) -> int:
        maxlen = [1] * len(nums)
        if (len(nums) == 1):
            return maxlen[0]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if (nums[i] > nums[j] and maxlen[j] + 1 > maxlen[i]):
                    maxlen[i] = maxlen[j] + 1
                    # print(maxlen)

        return max(maxlen)

#first pass
class Solution2:
    def lengthOfLIS(self, nums: [int]) -> int:
        sols = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    sols[i] = max(sols[i], sols[j] + 1)
        return max(sols)

# 833-851, 18 minutes. memory holds well. O(n^2) solution