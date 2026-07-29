class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Tortoise and Hare to find the intersection point
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]           # Move 1 step
            fast = nums[nums[fast]]     # Move 2 steps
            
            if slow == fast:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        slow = 0 # Move slow back to the start
        
        while slow != fast:
            slow = nums[slow] # Move 1 step
            fast = nums[fast] # Move 1 step
            
        return slow