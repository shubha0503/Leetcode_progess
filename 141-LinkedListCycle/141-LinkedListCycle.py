# Last updated: 7/4/2026, 10:44:41 AM
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move 1 step
            fast = fast.next.next     # move 2 steps

            if slow == fast:
                return True

        return False
