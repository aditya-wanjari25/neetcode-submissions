class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # PHASE 1: Find middle and break the list
        slow = head
        fast = head.next # Offset by 1 so slow lands at the end of the left half

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is at the end of the left half. The right half starts at slow.next
        second_half = slow.next
        slow.next = None   # break the list cleanly!

        # PHASE 2: Reverse the second half
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # PHASE 3: Merge the two halves
        # We don't strictly need a dummy node, but your logic works perfectly with it!
        dummy = ListNode()
        tail = dummy
        
        list1 = head
        list2 = prev # prev is the head of the reversed second half
        
        while list1 or list2:
            if list1:
                tail.next = list1
                tail = list1         # Move tail forward
                list1 = list1.next
            
            if list2:
                tail.next = list2
                tail = list2         # Added the missing tail update!
                list2 = list2.next
                
    