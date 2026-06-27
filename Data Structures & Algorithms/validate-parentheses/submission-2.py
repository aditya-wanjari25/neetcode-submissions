class Solution:
    def isValid(self, s: str) -> bool:
        p_hash = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        stack = []
        for char in s:
            if char in p_hash.keys():
                stack.append(char)
            
            else:
                if stack and p_hash[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        
        return len(stack) == 0
