# Last updated: 8/21/2026, 11:07:01 AM
1class Solution:
2    def findKthSmallest(self, coins: List[int], k: int) -> int:
3        def check(mx: int) -> bool:
4            cnt = 0
5            for i in range(1, 1 << len(coins)):
6                v = 1
7                for j, x in enumerate(coins):
8                    if i >> j & 1:
9                        v = lcm(v, x)
10                        if v > mx:
11                            break
12                m = i.bit_count()
13                if m & 1:
14                    cnt += mx // v
15                else:
16                    cnt -= mx // v
17            return cnt >= k
18
19        return bisect_left(range(10**11), True, key=check)