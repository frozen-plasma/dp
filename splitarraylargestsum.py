#optimal pass, not my work
class Solution1:
    def splitArray(self, nums: [int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            count, cur = 1, 0
            for num in nums:
                cur += num
                if cur > mid:
                    cur = num
                    count += 1
                    print("two", cur, mid, count)
            if count > m:
                l = mid + 1
            else:
                r = mid
        return l
#first pass - concept, does not fully work
class Solution2:
    def splitArray(self, nums: [int], m: int) -> int:
        ls = 0
        rs = len(nums) - m + 1
        ret = float('inf')
        self.tmpsums = []
        self.tmparr = []
        while ls < rs:
            #print("\n")
            self.tmpsums = []
            #self.tmparr.append(sum(nums[:ls+1]))
            self.splitsum(m, nums) #self.splitsum(m - 1, nums[ls + 1:])
            #print("tempsums", self.tmpsums)
            if self.tmpsums:
                ret = min(ret, min(self.tmpsums))
            ls += 1
            #print(ret)
        return ret

    def splitsum(self, n, arr):
        l = 0
        r = len(arr) - n + 1
        while l < r:
            #print(n, arr)
            if len(arr) == 1:
                #print("1", arr[0])
                self.tmparr.append(arr[0])
                #print("tmparr", self.tmparr)
            elif n == 1:
                tmpsum = 0
                for i in range(1, len(arr)):
                    tmpsum = max(tmpsum, sum(arr[:i] + arr[i:]))
                #print("n==1", arr, tmpsum)
                self.tmparr.append(tmpsum)
                #print("tmparr", self.tmparr)
            else:
                #print("splits left", n, arr)
                self.tmparr.append(sum(arr[:l + 1]))
                self.splitsum(n - 1, arr[l + 1:])
                #print("tmparr", self.tmparr)
            if self.tmparr:
                self.tmpsums.append(max(self.tmparr))
            #print("tmparr", self.tmparr)
            self.tmparr = []
            l += 1
        return


# 750
'''
[1,2,3,4,5] 2
[1,2,3,4,5] 3
[1,2,3,4,5] 4
'''