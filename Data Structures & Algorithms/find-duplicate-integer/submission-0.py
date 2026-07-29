class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count_dict = {}

        for n in nums:
            if n in count_dict:
                return n
            else:
                count_dict[n] = 1
        