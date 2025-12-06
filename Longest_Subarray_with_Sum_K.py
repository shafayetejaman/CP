class Solution:
    def longestSubarray(self, arr, k):
        m = {0: -1}
        currSum = 0
        ans = 0

        for i in range(len(arr)):
            currSum += arr[i]
            x = currSum - k

            if x in m:
                ans = max(ans, i - m[x])

            m[currSum] = min(m.get(currSum, i), i)

        return ans
