class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target_map = {}
        for char in s1:
            target_map[char] = target_map.get(char, 0) + 1
        

        left = 0
        window = {}

        for right in range(len(s2)):
            # add the char to the window with its count
            window[s2[right]] = window.get(s2[right],0) + 1

            # if window > target, remove left most element from window
            if (right - left + 1) > len(s1):
                left_char = s2[left]
                window[left_char] -= 1 #reduce for dupes
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
            
            # check for match
            if window == target_map:
                return True
        
        return False


