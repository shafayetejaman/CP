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
    N, K, arr = inputer()
    cnt = l = 0
    m = AutoCleanDict()

    for r in range(N):
        m.add(arr[r], 1)
        while len(m) > K:
            m.add(arr[l], -1)
            l += 1
        cnt += r - l + 1

    return cnt


# t = int(input())
t = 1
for _ in range(t):
    print(main())
