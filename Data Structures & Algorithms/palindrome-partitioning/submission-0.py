class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_palindrome(sub: str) -> bool:
            i , j = 0, len(sub) - 1
            while i<j:
                if sub[i] != sub[j]:
                    return False
                i+= 1
                j -= 1
            
            return True


        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return
            
            for i in range(start, len(s)):
                sub = s[start:i+1]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(i+1)
                    path.pop()
            
        backtrack(0)
        return result



            


        