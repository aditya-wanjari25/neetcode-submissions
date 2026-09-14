class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start_index, current_subset):
            res.append(current_subset[:])

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                
                current_subset.append(nums[i])

                backtrack(i+1, current_subset)
                current_subset.pop()

        backtrack(0,[])
        return res    