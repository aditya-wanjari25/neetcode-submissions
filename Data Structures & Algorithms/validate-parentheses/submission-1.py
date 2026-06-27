class Solution:
    def isValid(self, s: str) -> bool:
        p_hash = {
            '(':')',
            '[':']',
            '{':'}'
        }
        open_p = ['(','{','[']
        close_p = [')','}',']']
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] in open_p:
                stack.append(s[i])
            
            else:
                if len(stack) > 0 and (p_hash[stack[-1]] == s[i]):
                    stack.pop()
                else:
                    return False
            i+=1

        if len(stack) == 0:
            return True
        else:
            return False
