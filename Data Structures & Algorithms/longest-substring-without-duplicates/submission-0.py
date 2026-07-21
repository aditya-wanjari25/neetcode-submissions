class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        lookup = set()
        max_len = 0
        while right < len(s):
            if s[right] not in lookup:
                lookup.add(s[right])
                max_len = max(right - left + 1, max_len)
                right += 1
            else:
                lookup.remove(s[left])
                left += 1
        
        return max_len


         