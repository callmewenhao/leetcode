# -*- coding: utf-8 -*-

"""
@File    : isRobotBounded.py
@Author  : wenhao
@Time    : 2023/4/11 8:46
@LC      : 1041
"""
from collections import Counter


class Solution:
    # fuck 😖 机器人想要摆脱循环，在一串指令之后的状态，必须是不位于原点且方向朝北
    # 我的思路
    # 分析机器人的移动性质
    # 如果有环 移动 4 次必然回到原点 方向也一致
    # 甚至 2 次就有可能回到原点
    def isRobotBounded(self, instructions: str) -> bool:
        # d = [0, 1, 2, 3]  # 北 东 南 西

        move = [0, 0, 0]  # 坐标 0,0  方向 0
        for _ in range(4):
            for ch in instructions:
                if ch == 'L':
                    move[2] = (move[2] + 3) % 4
                if ch == 'R':
                    move[2] = (move[2] + 1) % 4
                if ch == 'G':
                    if move[2] == 0:
                        move[1] += 1
                    if move[2] == 1:
                        move[0] += 1
                    if move[2] == 2:
                        move[1] -= 1
                    if move[2] == 3:
                        move[0] -= 1
        return all(x == 0 for x in move)  # 判断是否回到原点














