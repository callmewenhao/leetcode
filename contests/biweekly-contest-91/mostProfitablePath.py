from math import inf
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1  # size of tree node
        # build the graph
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        # find the bob time in the path!
        bob_time = [n] * n

        def dfs_bob(x: int, fa: int, t: int) -> bool:
            if x == 0:
                bob_time[0] = t
                return True
            find_0 = False
            for son in g[x]:
                if son != fa:
                    if dfs_bob(son, x, t + 1):
                        find_0 = True
                        # break
            if find_0:
                bob_time[x] = t
            return find_0

        dfs_bob(bob, -1, 0)

        # alice path to a new leaf node
        ans = -inf  # the answer
        g[0].append(-1)  # give root(0) another son node, in case of thinking root is a leaf

        def dfs_alice(x: int, fa: int, alice_time: int, tot: int) -> None:
            # if we meet a node with time alice_time
            if alice_time < bob_time[x]:
                tot += amount[x]
            elif alice_time == bob_time[x]:
                tot += amount[x] // 2

            # meet a leaf node
            if len(g[x]) == 1:
                nonlocal ans
                ans = max(ans, tot)
                return

            # meet not a leaf node
            for son in g[x]:
                if son != fa:
                    dfs_alice(son, x, alice_time + 1, tot)

        dfs_alice(0, -1, 0, 0)
        return ans
