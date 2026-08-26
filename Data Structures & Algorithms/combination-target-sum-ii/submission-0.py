class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()  # FIX 1: Sort in-place, don't reassign

        def backtrack(index, remain, subset):
            if remain == 0:
                output.append(subset.copy())  # FIX 2: Append a copy!
                return
            
            if remain < 0 or index == len(candidates):
                return
            
            # BRANCH 1: INCLUDE
            subset.append(candidates[index])
            backtrack(index + 1, remain - candidates[index], subset)
            
            # BACKTRACK (Clean up the backpack first)
            subset.pop()

            # BRANCH 2: EXCLUDE
            # FIX 3: Skip duplicates with a while loop
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, remain, subset)
        
        backtrack(0, target, [])
        return output