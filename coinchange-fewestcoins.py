#historical pass
class Solution1:
    def coinChange(self, coins: [int], amount: int) -> int:
        #print(coins, amount)
        maxs = [-1]*amount
        vals = [[-1 for x in range(amount)] for y in range(len(coins))]
        temp = []
        #print(vals, "\n")
        for amt in range(amount):
            for coin in range(len(coins)):
                #print("coin: ", coins[coin])
                if((amt+1)-coins[coin]<0):
                    vals[coin][amt]=-1
                elif((amt+1)-coins[coin]==0):
                    #print("amt-coin==0: ", amt, coins[coin])
                    vals[coin][amt]=1
                elif((amt+1)-coins[coin]>0):
                    if(maxs[(amt+1)-coins[coin]-1]==-1):
                        #print("no best previous answer: ", amt, coin)
                        vals[coin][amt]=-1
                    else:
                        #print("best previous answer found, placing at: ", amt, coin)
                        vals[coin][amt]=maxs[(amt+1)-coins[coin]-1]+1
            #print(amt+1, vals)

            for elem in vals:
                if(elem[amt]!=-1):
                    temp.append(elem[amt])
            try:
                maxs[amt] = min(temp)
            except:
                maxs[amt] = -1
            temp = []
            #print("maxs: ", maxs, "\n")
        try:
            return maxs[len(maxs)-1]
        except:
            return 0

#first pass not successful, this is the second pass:
class Solution2:
    def coinChange(self, coins: [int], amount: int) -> int:
        coins = sorted(coins)
        sols = [[float('inf') for j in range(amount + 1)] for i in range(len(coins) + 1)]
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                # print(coins[i-1], j)
                if j == 0:
                    sols[i][j] = 0
                    continue
                if j >= coins[i - 1]:
                    sols[i][j] = min(sols[i - 1][j], 1 + sols[i][j - coins[i - 1]])
                else:
                    sols[i][j] = sols[i - 1][j]
                # print(sols)
        return sols[-1][-1] if sols[-1][-1] != float('inf') else -1

# 722-731, O(n^2) time and space complexity

#third pass
class Solution3:
    def coinChange(self, coins: [int], amount: int) -> int:
        coins = sorted(coins)
        sols = [float('inf')] * (amount+1)
        for coin in coins:
            for i in range(amount+1):
                if i == 0:
                    sols[i] = 0
                    continue
                if i-coin >= 0:
                    sols[i] = min(sols[i], 1+sols[i-coin])
        return sols[-1] if sols[-1] != float('inf') else -1
#734-741, optimal.