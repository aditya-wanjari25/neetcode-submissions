class Solution:
    def countZero(self,nums):
        counter = 0
        for i in nums:
            if(i == 0):
                counter+=1
        return counter

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        zeros = self.countZero(nums)
        res = []
        if(zeros == 0):
            mul = 1
            for i in range(len(nums)):
                mul = mul * nums[i]
            
            for i in range(len(nums)):
                res.append((mul//nums[i]))
            
            
        elif (zeros == 1):
            idx = nums.index(0)
            mul = 1
            
            for i in nums:
                if i == 0: continue
                else: mul *= i
            
            for i in range(len(nums)):
                if i == idx:
                    res.append(mul)
                else:
                    res.append(0)
        else:
            res = [0] * len(nums)
        return res











