class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(subset):
            if len(subset) == len(nums):
                output.append(subset.copy())
                return
            
            for num in nums:
                if num in subset:
                    continue
            
                subset.append(num)
                backtrack(subset)

                subset.pop()
        
        backtrack([])
        return output    

        