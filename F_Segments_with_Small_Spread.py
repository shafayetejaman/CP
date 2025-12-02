from collections import deque, defaultdict, Counter
from bisect import bisect_left as lowerBound, bisect_right as upperBound
import math


def inputer():
    N, limit = map(int, input().split())
    arr = list(map(int, input().split()))
    return N, limit, arr


def main():
    N, limit, nums = inputer()

    maxQueue = deque()
    minQueue = deque()
    l = ans = 0

    for r in range(N):
        while maxQueue and nums[maxQueue[-1]] < nums[r]:
            maxQueue.pop()
        while minQueue and nums[minQueue[-1]] > nums[r]:
            minQueue.pop()

        maxQueue.append(r)
        minQueue.append(r)

        while nums[maxQueue[0]] - nums[minQueue[0]] > limit:
            if l >= maxQueue[0]:
                maxQueue.popleft()
            if l >= minQueue[0]:
                minQueue.popleft()
            l += 1
        ans += r - l + 1
    return ans


# t = int(input())
t = 1
for _ in range(t):
    print(main())
