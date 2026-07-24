# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address = {}
        tail = head

        while tail:
            if tail.next in address:
                return True
            else:
                address[tail.next] = 1
                tail = tail.next
        
        return False
        