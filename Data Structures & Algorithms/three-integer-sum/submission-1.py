class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # logic a+b+c = 0 ==> a+b = -c
        for i , num in enumerate(nums):
            
            # if c >0 , subsequent nos can never be > 0
            if num > 0 : break 

            # skipping over duplicates
            if i>0 and num == nums[i-1]:
                continue
            
            # 2pointer logic
            left, right = i+1, len(nums)-1
            while left<right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum <0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            
        return res
                    





                

     