# Last updated: 7/4/2026, 10:45:45 AM
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next
