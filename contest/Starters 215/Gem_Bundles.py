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
    return len(arr), arr
    # return N, K, arr


def main():
    N, arr = inputer()
    m = min(arr)
    ans = m * 10

    for i in range(N):
        arr[i] -= m
        ans += 3 * arr[i]

    return ans


t = int(input())
# t = 1
for _ in range(t):
    print(main())
