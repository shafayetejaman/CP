from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    return N, arr, S


def main():
    N, arr, S = inputer()
    l = currSum = 0
    minLen = float("inf")

    for r in range(N):
        currSum += arr[r]

        while currSum >= S:
            minLen = min(minLen, r - l + 1)
            currSum -= arr[l]
            l += 1

    return minLen if minLen != float("inf") else -1


t = 1
for _ in range(t):
    print(main())
