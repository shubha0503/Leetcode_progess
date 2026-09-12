// Last updated: 9/12/2026, 9:30:40 PM
1class Solution {
2    public int[] maximumWeight(List<List<Integer>> intervals) {
3        int n = intervals.size();
4        int[][] arr = new int[n][4];
5        for (int i = 0; i < n; ++i) {
6            List<Integer> e = intervals.get(i);
7            arr[i] = new int[] {e.get(0), e.get(1), e.get(2), i};
8        }
9        Arrays.sort(arr,
10            (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
11        int[] nxt = new int[n];
12        for (int i = 0; i < n; ++i) {
13            nxt[i] = search(arr, arr[i][1], i + 1);
14        }
15        long[][] f = new long[n + 1][5];
16        int[][][] g = new int[n + 1][5][];
17        for (int k = 0; k < 5; ++k) {
18            g[n][k] = new int[0];
19        }
20        for (int i = n - 1; i >= 0; --i) {
21            g[i][0] = new int[0];
22            for (int k = 1; k < 5; ++k) {
23                long s1 = f[i + 1][k];
24                int[] a1 = g[i + 1][k];
25                long s2 = f[nxt[i]][k - 1] + arr[i][2];
26                int[] a2 = insert(g[nxt[i]][k - 1], arr[i][3]);
27                if (s2 > s1 || (s2 == s1 && less(a2, a1))) {
28                    f[i][k] = s2;
29                    g[i][k] = a2;
30                } else {
31                    f[i][k] = s1;
32                    g[i][k] = a1;
33                }
34            }
35        }
36        return g[0][4];
37    }
38
39    private int search(int[][] arr, int x, int l) {
40        int r = arr.length;
41        while (l < r) {
42            int mid = (l + r) >> 1;
43            if (arr[mid][0] > x) {
44                r = mid;
45            } else {
46                l = mid + 1;
47            }
48        }
49        return l;
50    }
51
52    private int[] insert(int[] a, int x) {
53        int n = a.length;
54        int[] b = new int[n + 1];
55        int i = 0;
56        while (i < n && a[i] < x) {
57            b[i] = a[i];
58            ++i;
59        }
60        b[i] = x;
61        while (i < n) {
62            b[i + 1] = a[i];
63            ++i;
64        }
65        return b;
66    }
67
68    private boolean less(int[] a, int[] b) {
69        int m = Math.min(a.length, b.length);
70        for (int i = 0; i < m; ++i) {
71            if (a[i] != b[i]) {
72                return a[i] < b[i];
73            }
74        }
75        return a.length < b.length;
76    }
77}