from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


class AutoCleanDict(dict):
    def add(self, key, delta):
        new_val = self.get(key, 0) + delta
        if new_val == 0:
            self.pop(key, None)
        else:
            self[key] = new_val


def inputer():
    # N = int(input())
    N, K = map(int, input().split())
    fruits = list(map(int, input().split()))
    height = list(map(int, input().split()))
    # return N, arr
    return N, K, fruits, height


def main():
    N, k, fruits, height = inputer()
    ans = currSum = l = 0

    for r in range(N):
        currSum += fruits[r]

        while currSum > k:
            currSum -= fruits[l]
            l += 1

        if r > 0 and r > l and height[r - 1] % height[r] != 0:
            currSum = fruits[r]
            l = r

        ans = max(ans, r - l + 1)

    return ans


t = int(input())
# t = 1
for _ in range(t):
    print(main())
