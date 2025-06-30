from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N = int(input())
    # arr = list(map(int, input().split()))
    arr = [0] * N
    return N, arr


def main():
    N, arr = inputer()
    num = N
    for i in range(0, N // 2):
        arr[N - i - 1] = num
        arr[i] = num - 1
        num -= 2

    if N % 2 == 1:
        arr[N // 2] = 1

    return arr


t = int(input())
for _ in range(t):
    print(*main(), sep=" ")
