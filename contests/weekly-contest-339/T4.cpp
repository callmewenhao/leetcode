#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

/*

找规律 😁
公差为 2 的等差数列
左边界 max(i-k+1, k-i-1)
右端点 min(2n-k-i-1, i+k-1)

看到最少操作次数 能不能用 bfs 模拟
初始 p
每一步 把 [max(i-k+1, k-i-1), min(2n-k-i-1, i+k+1)] 内的 没有访问过
的下标放到对列中 暴力枚举 O(nk) 超时 优化 想办法去掉已经访问过的下标

1. 用平衡树 😂
维护下标 删除
技巧 两个平衡树维护 一个维护偶数下标 一个维护奇数下标

2. 用并查集 👍


*/

class Solution {
   public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        std::unordered_set<int> ban{banned.begin(), banned.end()};
        std::set<int> sets[2];
        for (int i = 0; i < n; i++) {
            if (i != p && !ban.count(i)) {
                sets[i % 2].insert(i);
            }
        }
        sets[0].insert(n); // 哨兵
        sets[1].insert(n);

        // BFS
        std::vector<int> ans(n, -1);
        std::vector<int> q{p};
        for (int step = 0; !q.empty(); step++) {
            vector<int> nq;
            for (int i : q) {
                ans[i] = step;
                int mn = max(i - k + 1, k - i - 1);
                int mx = min(i + k - 1, 2 * n - k - i - 1);
                auto& s = sets[mn % 2];
                for (auto it = s.lower_bound(mn); *it <= mx; it = s.erase(it)) {
                    nq.push_back(*it);
                }
            }
            q = std::move(nq);
        }
        return ans;
    }
};
