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
    arr = list(map(int, input().split()))
    # return N, arr
    return N, K, arr


def main():
    N, k, arr = inputer()
    mLen = l = currSum = 0

    for r in range(N):
        currSum += arr[r]
        while currSum > k:
            currSum -= arr[l]
            l += 1
        if currSum == k:
            mLen = max(mLen, r - l + 1)

    return N - mLen if mLen > 0 else -1


t = int(input())
# t = 1
for _ in range(t):
    print(main())
