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

def maxProduct2(self, nums: [int]) -> int:
    if len(nums) == 1:
        return nums[0]
    possols = [nums[0]]
    negsols = [nums[0]]
    sols = [nums[0]]
    for i in range(1, len(nums)):
        negsols.append(min(nums[i], nums[i]*possols[i-1], nums[i]*negsols[i-1]))
        possols.append(max(nums[i], nums[i]*negsols[i-1], nums[i]*possols[i-1]))
        sols.append(max(possols[-1], negsols[-1]))
    #print(possols, "\n", negsols, "\n", sols)
    return max(sols)
#over time, revisit