#first pass
def maxSubArray(self, nums: [int]) -> int:
    dpsums = [nums[0]]
    summ = 0
    if (len(nums) == 1):
        return nums[0]
    for i in range(1, len(nums)):
        curr = nums[i]
        prev = dpsums[i - 1]
        if (nums[i] >= 0 and dpsums[i - 1] < 0):
            prev = 0
        summ = prev + nums[i]
        # print("curr prev sum: ", curr, prev, summ)
        dpsums.append(max(curr, summ))
        # print(dpsums[i-1], nums[i], dpsums[i-1]+nums[i])
        # print(dpsums)
    return max(dpsums)
#second pass

def maxSubArray2(self, nums: [int]) -> int:
    if len(nums) == 1:
        return nums[0]
    sols = [nums[0]]
    for i in range(1, len(nums)):
        sols.append(max(sols[i - 1] + nums[i], nums[i]))
    print(sols)
    return max(sols)

# 5 minutes