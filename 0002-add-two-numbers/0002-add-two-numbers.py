# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Dummy node to start the result list
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Step 2: Iterate while there are nodes or a remaining carry
        while l1 or l2 or carry:
            # Get values (default to 0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total and new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create new node and move pointer
            curr.next = ListNode(new_val)
            curr = curr.next
            
            # Move l1 and l2 if possible
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next