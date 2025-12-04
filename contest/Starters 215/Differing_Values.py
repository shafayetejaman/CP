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
    s = input()
    # return N, arr
    return N, K, s


def main():
    N, K, s = inputer()

    cnt = Counter(s)
    ones, zeros = cnt["1"], cnt["0"]

    for i in range(K):
        count = math.ceil((N - i) / K)

        ones -= count // 2
        zeros -= count // 2

        if count % 2 == 1:
            if ones > zeros:
                ones -= 1
            else:
                zeros -= 1

    if min(ones, zeros) < 0:
        return "No"

    return "Yes"


t = int(input())
# t = 1
for _ in range(t):
    print(main())
