from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    return N, arr1, arr2


def main():
    N, arrival, departure = inputer()
    arr = [(i, 1) for i in arrival]
    arr.extend([(i, 0) for i in departure])
    arr.sort()
    cnt = ans = 0

    for i in range(N * 2):
        if arr[i][1]:
            cnt += 1
        else:
            cnt -= 1
        ans = max(ans, cnt)

    return ans


t = int(input())
for _ in range(t):
    print(main())
