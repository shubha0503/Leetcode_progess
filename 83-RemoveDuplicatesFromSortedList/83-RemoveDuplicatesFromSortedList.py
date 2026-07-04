# Last updated: 7/4/2026, 10:45:17 AM
class Solution(object):
    def deleteDuplicates(self, head):
        current = head 
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
     