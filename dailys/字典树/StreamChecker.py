# -*- coding: utf-8 -*-

"""
@File    : StreamChecker.py
@Author  : wenhao
@Time    : 2023/3/24 12:43
@LC      : 1032
"""
from typing import List


# 字典树模板 😁
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    # 关键函数 插入 word 建字典树 Tire
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    # 这个函数与 之前写的不一样
    # 判断字典树中的字符串 是否是 s 的前缀 和之前的任务刚好相反🧐
    def find(self, s: str) -> bool:
        node = self
        for ch in s:
            ch = ord(ch) - ord("a")
            if node.isEnd:  # 遇到末端就返回 True
                return True
            if not node.children[ch]:  # 如果遇到没见过的节点就返回 False
                return False
            node = node.children[ch]
        return node.isEnd  # 如果走到了最后看末端


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.buf = []
        for word in words:
            self.trie.insert(word[::-1])  # 逆序存放

    def query(self, letter: str) -> bool:
        self.buf.append(letter)
        if len(self.buf) > 200:  # 根据题目维护一个 200 大小的 buf
            self.buf.pop(0)
        return self.trie.find(''.join(self.buf)[::-1])  # 反转匹配

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
