#first pass, naive. 904-936, 32 minutes
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = ""
        # fill with longest palindrone to that point
        if len(s) == 1:
            return s
        tok = False
        for i in range(len(s)):
            curr = s[i]
            tmp = len(s) - 1
            while tmp >= i:
                curr2 = s[tmp]
                if curr == curr2:
                    res = self.checkPal(s[i:tmp + 1])
                    if res and len(res) > len(sol):
                        sol = res
                tmp -= 1
        # print("sols", sols)
        return sol

    def checkPal(self, s):
        notpal = False
        # print("potential pal :", s)
        for i in range(0, int(len(s) / 2)):
            if s[i] == s[-1 - i]:
                continue
            else:
                notpal = True
                break
        if notpal:
            return None
        else:
            return s
#works but exceeds time limit. O(n^3)

#second pass
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = ""
        self.tmp = ""
        self.rightclose = False
        self.leftclose = False
        for i in range(len(s)):
            self.tmp = ""
            self.rightclose = False
            self.leftclose = False
            self.rcheck(s, i, 0)
            if len(self.tmp) > len(lp):
                lp = self.tmp
            # print(lp)
        return lp

    def rcheck(self, s, i, k):
        if k == 0 and not self.tmp:
            self.tmp = s[i]
            self.rcheck(s, i, 1)
            return
        else:
            if i + k < len(s) and i - k >= 0 and self.rightclose == False and self.leftclose == False:
                if s[i + k] == s[i - k]:
                    self.tmp = s[i - k] + self.tmp
                    self.tmp = self.tmp + s[i + k]
                    self.rcheck(s, i, k + 1)
                    return
                elif s[i + k] == s[i + k - 1] == s[i] and self.rightclose == False:
                    self.tmp = self.tmp + s[i + k]
                    self.leftclose = True
                    self.rcheck(s, i, k + 1)

                    return
                elif s[i - k] == s[i - k + 1] == s[i] and self.leftclose == False:
                    self.tmp = s[i - k] + self.tmp
                    self.rightclose = True
                    self.rcheck(s, i, k + 1)

                    return
                else:
                    return
            elif i + k < len(s):
                if s[i + k] == s[i + k - 1] == s[i] and self.rightclose == False:
                    self.tmp = self.tmp + s[i + k]
                    self.leftclose = True
                    self.rcheck(s, i, k + 1)

                else:
                    return
            elif i - k >= 0:
                if s[i - k] == s[i - k + 1] == s[i] and self.leftclose == False:
                    self.tmp = s[i - k] + self.tmp
                    self.rightclose = True
                    self.rcheck(s, i, k + 1)

                    return
                else:
                    return
            else:
                return
# 656-746, 50 minutes. only works for single letter palindromes.

#third pass
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = s[0]
        for i in range(1, len(s)):
            tmp = self.rcheck(s, i, i)
            tmp2 = self.rcheck(s, i - 1, i)
            # print(tmp, tmp2)
            lp = max([lp, tmp, tmp2], key=len)
        return lp

    def rcheck(self, s, i1, i2):
        while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
            i1 -= 1
            i2 += 1
        return s[i1 + 1:i2]

# 813-826, 13 minutes. looked at optimal solution for this pass. notice how the cases for 'odd' and 'even' palindromes
# must be separate. notice the elegant pointer incrementation for palindrome checking.