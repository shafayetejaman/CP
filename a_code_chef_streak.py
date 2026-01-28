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
    om = list(map(int, input().split()))
    addy= list(map(int, input().split())) 
    return N,  om , addy
    # return N, K, arr


def main():
    N, om, addy= inputer()
    
    cntOm =cntAddy= cnt= 0

    for val in om:
        if val:
            cnt+=1
        else:
            cntOm = max(cntOm, cnt)
            cnt=0

    cntOm = max(cntOm, cnt)
    cnt = 0
    for val in addy:
        if val:
            cnt+=1
        else:
            cntAddy = max(cntAddy, cnt)
            cnt=0

    cntAddy = max(cntAddy, cnt)
    return "Addy" if cntAddy > cntOm else "Draw" if cntOm == cntAddy else "Om"


t = int(input())
# t = 1
for _ in range(t):
    print(main())

