# Last updated: 8/31/2026, 9:52:22 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        ans = [inf, -inf]
9        first = last = -1
10        i = 0
11        while head.next.next:
12            a, b, c = head.val, head.next.val, head.next.next.val
13            if a > b < c or a < b > c:
14                if last == -1:
15                    first = last = i
16                else:
17                    ans[0] = min(ans[0], i - last)
18                    last = i
19                    ans[1] = max(ans[1], last - first)
20            i += 1
21            head = head.next
22        return [-1, -1] if first == last else ans