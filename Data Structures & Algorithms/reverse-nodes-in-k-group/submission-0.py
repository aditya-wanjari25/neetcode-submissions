class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. Probe ahead k steps
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break  # Not enough nodes left, we are done!
                
            groupNext = kth.next
            
            # 2. Reverse the group
            # BRILLIANT TRICK: Instead of starting 'prev' at None, we start it at 'groupNext'.
            # This automatically connects the tail of our newly reversed list to the next chunk!
            prev = kth.next 
            curr = groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # 3. Reconnect the boundaries
            # groupPrev.next is currently pointing to the OLD head (which is now the tail).
            # We save it, update groupPrev to point to the NEW head (kth), 
            # and then slide groupPrev forward to the old head to prep for the next loop.
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next

    # Helper function just to walk forward k steps
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr