class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # STEP 1: Clone and interweave
        current = head
        while current:
            # Save the future
            next_original = current.next
            
            # Create the clone and wedge it in between current and next_original
            clone = Node(current.val)
            current.next = clone
            clone.next = next_original
            
            # Move forward
            current = next_original
            
        # STEP 2: Assign random pointers to the clones
        current = head
        while current:
            if current.random:
                # The clone is at current.next. 
                # Its random should be the node immediately following the original's random.
                current.next.random = current.random.next
            current = current.next.next # Skip over the clone to the next original
            
        # STEP 3: Unweave to restore the original list and extract the copy
        current = head
        copied_head = head.next # The start of our new cloned list
        
        while current:
            clone = current.next
            
            # Restore the original list's next pointer
            current.next = clone.next
            
            # Setup the clone's next pointer (if we aren't at the end)
            if clone.next:
                clone.next = clone.next.next
                
            current = current.next
            
        return copied_head