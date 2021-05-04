#pass one
def maxProduct(self, nums: [int]) -> int:
    maxpos = nums[0]
    maxneg = nums[0]
    prod = (-(float('inf')))
    temp = 0
    if(len(nums)==1):
        return maxpos
    for i in range(len(nums)):
        if(i==0):
            print(maxpos, maxneg)
            prod = maxpos
            continue
        tempneg = maxneg
        temppos = max(nums[i], maxpos*nums[i], maxneg*nums[i])
        maxneg = min(nums[i], maxpos*nums[i], maxneg*nums[i])
        maxpos = temppos
        prod = max(maxpos, prod)
        if(nums[i]<0):
            if(tempneg*nums[i]!=maxpos):
                maxpos = 1
    return prod

#pass two