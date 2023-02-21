# -*- coding: utf-8 -*-

"""
@File    : videoStitching.py
@Author  : wenhao
@Time    : 2023/2/21 10:13
@LC      : 1024
"""
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: x[0])  # 区间问题排序
        # print(clips)

        # 初始位置 [0,0]
        e = 0
        ans = 0

        i, n = 0, len(clips)
        while e < time:
            # 寻找新的 end
            # 贪心：必定是能够接触的最远的 end
            e_ = e
            while i < n and clips[i][0] <= e:  # 保证能够接触
                if e_ < clips[i][1]:
                    e_ = clips[i][1]
                i += 1
            ans += 1

            # end 没变代表 视频不连续！
            if e_ == e:
                return -1
            e = e_  # 更新
        return ans











