# Last updated: 8/13/2026, 2:28:14 PM
1def max(a: int, b: int) -> int:
2    return a if a > b else b
3
4
5class Node:
6    __slots__ = "l", "r", "lmx", "rmx", "mx"
7
8    def __init__(self, l: int, r: int):
9        self.l = l
10        self.r = r
11        self.lmx = self.rmx = self.mx = 1
12
13
14class SegmentTree:
15    __slots__ = "s", "tr"
16
17    def __init__(self, s: str):
18        self.s = list(s)
19        n = len(s)
20        self.tr: List[Node | None] = [None] * (n * 4)
21        self.build(1, 1, n)
22
23    def build(self, u: int, l: int, r: int):
24        self.tr[u] = Node(l, r)
25        if l == r:
26            return
27        mid = (l + r) // 2
28        self.build(u << 1, l, mid)
29        self.build(u << 1 | 1, mid + 1, r)
30        self.pushup(u)
31
32    def query(self, u: int, l: int, r: int) -> int:
33        if self.tr[u].l >= l and self.tr[u].r <= r:
34            return self.tr[u].mx
35        mid = (self.tr[u].l + self.tr[u].r) // 2
36        ans = 0
37        if r <= mid:
38            ans = self.query(u << 1, l, r)
39        if l > mid:
40            ans = max(ans, self.query(u << 1 | 1, l, r))
41        return ans
42
43    def modify(self, u: int, x: int, v: str):
44        if self.tr[u].l == self.tr[u].r:
45            self.s[x - 1] = v
46            return
47        mid = (self.tr[u].l + self.tr[u].r) // 2
48        if x <= mid:
49            self.modify(u << 1, x, v)
50        else:
51            self.modify(u << 1 | 1, x, v)
52        self.pushup(u)
53
54    def pushup(self, u: int):
55        root, left, right = self.tr[u], self.tr[u << 1], self.tr[u << 1 | 1]
56        root.lmx = left.lmx
57        root.rmx = right.rmx
58        root.mx = max(left.mx, right.mx)
59        a, b = left.r - left.l + 1, right.r - right.l + 1
60        if self.s[left.r - 1] == self.s[right.l - 1]:
61            if left.lmx == a:
62                root.lmx += right.lmx
63            if right.rmx == b:
64                root.rmx += left.rmx
65            root.mx = max(root.mx, left.rmx + right.lmx)
66
67
68class Solution:
69    def longestRepeating(
70        self, s: str, queryCharacters: str, queryIndices: List[int]
71    ) -> List[int]:
72        tree = SegmentTree(s)
73        ans = []
74        for x, v in zip(queryIndices, queryCharacters):
75            tree.modify(1, x + 1, v)
76            ans.append(tree.query(1, 1, len(s)))
77        return ans