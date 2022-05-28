
from typing import List


class Solution:
    def findSubsequence(self, a: List[int]) -> List[int]:
        n = len(a)
        if n == 0 or n == 1:
            return a
        trace = {0: -1}
        l = [0] # l[i] = j : a[j] là phần tử nhỏ nhất trong các phần tử cuối cùng của dãy có độ dài i
        d = 0 # độ dài lớn nhất của dãy kết quả
        for i in range(1, n):
            if a[i] <= a[l[0]]:
                l[0] = i
                trace[i] = -1
            elif a[i] >= a[l[d]]:
                trace[i] = l[d]
                d += 1
                l.append(i)
            else:
                t = self.binarySearchLeft(a, l, a[i])
                trace[i] = l[t - 1]
                l[t] = i

        i = l[d]
        result = []
        while i != -1:
            result.insert(0, a[i])
            i = trace[i]
        return result

    # Tìm vị trí i nhỏ nhất thoả mãn a[i] >= x
    def binarySearchLeft(self, a: List[int], l: List[int], x: int) -> int:
        b = 0
        e = len(l)

        while b <= e:
            p = (b + e) // 2
            if x <= a[l[p]]:
                e = p - 1
            elif x > a[l[p]]:
                b = p + 1

        return b


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequence([10, 9, 2, 5, 5, 5, 5, 5, 3, 4]))
