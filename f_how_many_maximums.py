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
    N = int(input())
    # N, K = map(int, input().split())
    # arr = list(map(int, input().split()))
    s = input()
    return N, s
    # return N, K, arr


def main():
    N, s = inputer()
    cnt = 0

    s = "0" + s + "1"

    for i in range(1, N + 2):
        cnt += 1 if s[i - 1] == "0" and s[i] == "1" else 0

    return cnt


t = int(input())
# t = 1
for _ in range(t):
    print(main())
