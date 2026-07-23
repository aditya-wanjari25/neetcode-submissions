'''
golden formula : 
size of window - freq of max element in the window = replacements
if replacements > k shrink the window
count max output in every iteration

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            
            max_freq = max(window.values())
            if (right - left + 1) - max_freq <= k:
                max_len = max(max_len, right - left + 1)
            
            else:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        
        return max_len

        