class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        prev = {}
        max_len = idx_start = idx = 0
        for idx,s_ in enumerate(s):
            if s_ in prev:
                if prev[s_] >= idx_start:
                    max_len = max(max_len,idx-idx_start)
                    idx_start = prev[s_]+1
            prev[s_] = idx
        return max(max_len,idx+1-idx_start)
        