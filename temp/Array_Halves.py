from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N = int(input())
    arr = list(map(int, input().split()))
    return N, arr


def main():
    N, arr = inputer()


t = int(input())
for _ in range(t):
    print(main())
