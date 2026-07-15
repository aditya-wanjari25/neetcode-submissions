class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1 
        
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] == target:
                return mid
            
            
            if target >= nums[mid]:
            # Check if left half is sorted
            # Or target is smaller than the leftmost element

                if nums[left] <= nums[mid] or target < nums[left]:
                    # go right
                    left = mid + 1
                else:
                    right = mid -1
            else:
                if nums[mid] <= nums[right] or target > nums[right]:
                    # go left
                    right = mid -1
                else:
                    left = mid + 1


        return -1