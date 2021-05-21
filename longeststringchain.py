#first pass
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: [str]) -> int:
        # q1. how to tell that word1 is pre of word2? datastructure must preserve order
        words.sort(key=lambda x: len(x))
        # print(words)
        sols = [1] * len(words)
        d = defaultdict(defaultdict)
        for i in range(1, len(words)):
            for j in range(0, i):
                word1, word2 = words[i], words[j]
                if self.pre(word2, word1):
                    sols[i] = max(sols[i], sols[j] + 1)
                    # print(sols[i])
        return max(sols)

    def pre(self, word2, word1):
        # print(word2, word1)
        oneout = False
        i = 0
        j = 0
        while i < len(word1):
            # print(word1[i], i, len(word1), j)
            if j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if oneout:
                    return False
                else:
                    oneout = True
                    i += 1
        if oneout and len(word2) + 1 == len(word1):
            return True
        else:
            return False

# 803-845, 42 minutes. used variation of LIS to solve, but is O(n*m^2)