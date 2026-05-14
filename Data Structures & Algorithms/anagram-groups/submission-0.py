class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for st in strs:
            counter = [0]*26
            for ch in st:
                counter[ord(ch) - ord('a')] += 1
            counter = tuple(counter)
            if counter in result:
                result[counter].append(st)
            else:
                result[counter] = [st]
        return list(result.values())
        