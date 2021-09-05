from typing import List


class Solution:
    def computeLevenshteinDistance(self, X: str, Y: str) -> int:
        n = len(X)
        m = len(Y)
        # khởi tạo ma trận levenshtein
        l = [[0 for j in range(m + 1)] for i in range(n + 1)]
        ## nếu Y là xâu rỗng để biến đổi Xi thành Y ta phải xoá đi i ký tự
        for i in range(0, n + 1):
            l[i][0] = i
        ## nếu X là xâu rỗng để biến đổi X thành Yj ta cần xoá đi j ký tự
        for j in range(0, m + 1):
            l[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if X[i - 1] == Y[j - 1]:
                    l[i][j] = l[i - 1][j - 1]
                else:
                    l[i][j] = min(l[i - 1][j], l[i][j - 1], l[i - 1][j - 1]) + 1

        return l[n][m]

    def printMatrix(self, l: List[List]):
        for i in range(0, len(l)):
            print("{}\n".format(l[i]))


if __name__ == '__main__':
    sol = Solution()
    print(sol.computeLevenshteinDistance("kitten", "sitting"))
