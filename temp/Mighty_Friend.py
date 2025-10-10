from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    return N, arr, k


def main():
    N, arr, k = inputer()
    aby = [val for idx, val in enumerate(arr) if idx % 2 == 0]
    bob = [val for idx, val in enumerate(arr) if idx % 2 == 1]

    aby.sort(reverse=True)
    bob.sort()

    for idx, val in enumerate(bob):
        if k == 0:
            break
        if aby[idx] > val:
            bob[idx], aby[idx] = aby[idx], bob[idx]
        else:
            break
        k -= 1

    return "YES" if sum(bob) > sum(aby) else "NO"


t = int(input())
for _ in range(t):
    print(main())
