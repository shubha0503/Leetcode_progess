# Last updated: 10/1/2026, 7:18:42 PM
1class Node:
2    __slots__ = "l", "r", "prod", "cnt"
3
4    def __init__(self, l: int, r: int, k: int):
5        self.l = l
6        self.r = r
7        self.prod = 1
8        self.cnt = [0] * k
9
10
11class SegmentTree:
12    __slots__ = "k", "tr"
13
14    def __init__(self, nums: list[int], k: int):
15        self.k = k
16        n = len(nums)
17        self.tr = [None] * (n << 2)
18        self.build(1, 1, n, nums)
19
20    def merge(self, a: Node, b: Node) -> tuple[int, list[int]]:
21        k = self.k
22        prod = a.prod * b.prod % k
23        cnt = a.cnt[:]
24        for r, c in enumerate(b.cnt):
25            cnt[a.prod * r % k] += c
26        return prod, cnt
27
28    def pushup(self, u: int):
29        prod, cnt = self.merge(self.tr[u << 1], self.tr[u << 1 | 1])
30        self.tr[u].prod = prod
31        self.tr[u].cnt = cnt
32
33    def build(self, u: int, l: int, r: int, nums: list[int]):
34        self.tr[u] = Node(l, r, self.k)
35        if l == r:
36            v = nums[l - 1] % self.k
37            self.tr[u].prod = v
38            self.tr[u].cnt[v] = 1
39            return
40        mid = (l + r) >> 1
41        self.build(u << 1, l, mid, nums)
42        self.build(u << 1 | 1, mid + 1, r, nums)
43        self.pushup(u)
44
45    def modify(self, u: int, x: int, v: int):
46        if self.tr[u].l == self.tr[u].r:
47            v %= self.k
48            self.tr[u].prod = v
49            self.tr[u].cnt = [0] * self.k
50            self.tr[u].cnt[v] = 1
51            return
52        mid = (self.tr[u].l + self.tr[u].r) >> 1
53        if x <= mid:
54            self.modify(u << 1, x, v)
55        else:
56            self.modify(u << 1 | 1, x, v)
57        self.pushup(u)
58
59    def query(self, u: int, l: int, r: int) -> Node:
60        if self.tr[u].l >= l and self.tr[u].r <= r:
61            return self.tr[u]
62        mid = (self.tr[u].l + self.tr[u].r) >> 1
63        if r <= mid:
64            return self.query(u << 1, l, r)
65        if l > mid:
66            return self.query(u << 1 | 1, l, r)
67        left = self.query(u << 1, l, r)
68        right = self.query(u << 1 | 1, l, r)
69        prod, cnt = self.merge(left, right)
70        res = Node(0, 0, self.k)
71        res.prod = prod
72        res.cnt = cnt
73        return res
74
75
76class Solution:
77    def resultArray(
78        self, nums: list[int], k: int, queries: list[list[int]]
79    ) -> list[int]:
80        n = len(nums)
81        tree = SegmentTree(nums, k)
82        ans = []
83        for idx, val, start, x in queries:
84            tree.modify(1, idx + 1, val)
85            ans.append(tree.query(1, start + 1, n).cnt[x])
86        return ans