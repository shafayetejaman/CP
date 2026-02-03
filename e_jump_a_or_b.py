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


yes = "Yes"
no = "No"


def inputer():
    # N = int(input())
    N, M, A, B = map(int, input().split())
    # arr = list(map(int, input().split()))
    return N, M, A, B
    # return N, K, arr


def main():
    N, M, A, B = inputer()
    ans = None
    db = {}
    A, B = max(A, B), min(A, B)

    if A * N < M:
        return no

    x = (M - N * B) / (A - B)

    ans = yes if (M - N * B) >= 0 and int(x) == x else no

    return ans


t = int(input())
# t = 1
for _ in range(t):
    print(main())
