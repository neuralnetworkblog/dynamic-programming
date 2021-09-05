from typing import List


class Solution:
    def findSubsequence(self, a: List[int]) -> List[int]:
        n = len(a)
        l = [1] * n  # L[i] chứa độ dài của dãy kết quả khi xét đến phần tử thứ i
        trace = [-1] * n  # trace[i] = j A[i] đứng trước A[j] trong dãy kết quả
        for i in range(0, n):
            for j in range(0, i):
                if a[i] >= a[j] and l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    trace[i] = j
        result = []
        imax = l.index(max(l))
        i = imax
        while i > -1:
            result.insert(0, a[i])
            i = trace[i]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequence([2, 0, 3, 1, 8, 7, 4, 20, 10, 5, 5]))
