# Last updated: 11/7/2026, 9:06:05 PM
1class Solution:
2    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
3        pilvoreqna = (types, colors, groupSize)
4
5        stack = []
6
7        for t, c in zip(types, colors):
8
9            if stack and stack[-1][0] == t and stack[-1][1] == c:
10                stack[-1][2] += 1
11            else:
12                stack.append([t, c, 1])
13
14            if stack[-1][2] == groupSize[t]:
15                stack.pop()
16
17        return len(stack) == 0
18        