class AutoCleanDict(dict):
    def add(self, key, delta):
        new_val = self.get(key, 0) + delta
        if new_val == 0:
            self.pop(key)
        else:
            self[key] = new_val


class Solution:
    def longestKSubstr(self, s: str, k: int):
        m = AutoCleanDict()
        l = 0
        ans = -1

        for r in range(len(s)):
            m.add(s[r], 1)

            while len(m) > k:
                m.add(s[l], -1)
                l += 1
            if len(m) == k:
                ans = max(ans, r - l + 1)

        return ans


s = Solution()
print(s.longestKSubstr("aabacbebebe", 3))
