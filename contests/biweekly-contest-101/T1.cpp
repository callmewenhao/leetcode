#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        int mask1 = 0, mask2 = 0;
        for (int num: nums1) mask1 |= (1 << num);
        for (int num: nums2) mask2 |= (1 << num);
        if (int mask = mask1 & mask2; mask) 
            return __builtin_ctz(mask);  // 返回数字二进制尾部 0 个数
        int m1 = __builtin_ctz(mask1);
        int m2 = __builtin_ctz(mask2);
        return min(m1 * 10 + m2, m2 * 10 + m1);
    }
};
