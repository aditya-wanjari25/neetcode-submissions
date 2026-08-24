class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(index, remain, current_subset):

            if remain == 0:
                output.append(current_subset.copy())
                return
            
            if remain < 0 or index == len(nums):
                return
            
            current_subset.append(nums[index])
            backtrack(index, remain - nums[index], current_subset)

            current_subset.pop()
            backtrack(index+1, remain, current_subset)
        
        backtrack(0,target, [])
        return output
        