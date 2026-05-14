class Solution:
    def countChars(self, s):
        d = dict()
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return d

    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1)!= len(s2):
            return False
        return self.countChars(s1) == self.countChars(s2)
            