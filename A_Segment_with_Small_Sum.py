from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    return N, arr, S


def main():
    N, arr, S = inputer()
    maxLen = l = currSum = 0

    for r in range(N):
        currSum += arr[r]
        while currSum > S:
            currSum -= arr[l]
            l += 1
        if r >= l:
            maxLen = max(maxLen, r - l + 1)

    return maxLen


t = 1
for _ in range(t):
    print(main())
