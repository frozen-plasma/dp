#second pass; first pass unsuccessful
class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        # first return count of all positions with 1
        # add to this count the count of all squares of size 2+
        # q1: how to define a square?
        # q2: how can we tell if we've visited a square? use visited = set(), once you find a square of side x mark it as visited and add x^2+(x-1)^2...1^2

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i > 0 and j > 0 and matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

        return sum(map(sum, matrix))

# 628-635, but had to see solution

arr = [0, 1, 2]
arr.insert(1, "xd")
print(arr)