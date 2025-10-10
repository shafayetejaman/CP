from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N = int(input())
    # arr = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    return N, arr


def main():
    N, arr = inputer()
    _sum = 0

    for row in range(N - 1, -1, -1):
        col = 0
        _currSum = 0
        while row < N:
            _currSum += arr[row][col]
            col += 1
            row += 1
        _sum = max(_sum, _currSum)

    for col in range(1, N):
        row = 0
        _currSum = 0
        while col < N:
            _currSum += arr[row][col]
            col += 1
            row += 1
        _sum = max(_sum, _currSum)

    return _sum


t = int(input())
for _ in range(t):
    print(main())
