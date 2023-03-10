# -*- coding: utf-8 -*-

"""
@File    : judgeCircle.py
@Author  : wenhao
@Time    : 2023/3/9 22:30
@LC      : 657
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and  moves.count('L') ==  moves.count('R')
