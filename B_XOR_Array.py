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
    # N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    return arr
    # return N, K, arr


def main():
    N, l, r = inputer()

    ans = None
    print(7 ^ 8 ^ 15 ^ 23 ^ 38)
    print()

    return ans


t = int(input())
# t = 1
for _ in range(t):
    print(main())
