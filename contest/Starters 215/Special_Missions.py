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
    N, C = map(int, input().split())
    arr = list(map(int, input().split()))
    s = input()
    # return N, arr
    return N, C, arr, s


def main():
    N, C, arr, s = inputer()
    total = 0
    spSum = 0
    arr = zip(arr, s)
    arr = sorted(arr, key=lambda x: x[1])

    for val, c in arr:
        if c == "1" and total >= C:
            spSum += val
        elif c == "0":
            total += val

    spSum -= C

    if spSum > 0:
        total += spSum

    return total


t = int(input())
# t = 1
for _ in range(t):
    print(main())
