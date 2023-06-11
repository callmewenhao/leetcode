# -*- coding: utf-8 -*-

"""
@File    : Trie.py
@Author  : wenhao
@Time    : 2023/3/24 14:10
@LC      : 208
"""


# 字典树/前缀树 Trie 🤗
# 树如其名 树形结构存储数据 核心思想也很好理解
# 节点包含一个 isEnd bool 值 表示 从根到当前节点 是否代表一个字符串👏
# 有一个关键函数 insert 用于把字符串插入这棵字典树 ✔️
# 查找函数 find 则可以根据要求自己设计 👏
# 下面的字典树实现借鉴于 leetcode 官方代码

class Trie:

    def __init__(self):
        self.children = [None] * 26  # 每个节点都有 26 个孩子 None 代表目前还没有
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                # 如果没有建立这个节点 那就建节点 并继续访问接下来的字符
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True  # 末端标记

    # 这个函数服务于 search 和 startsWith
    # 函数基本功能是返回 能和 prefix 匹配的字符串对应的节点
    # 如果没有匹配的节点 返回 None
    # 注意：返回节点并不一定代表字典树中含有 prefix 字符串 只说明含有 prefix 前缀
    def find(self, prefix: str):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return None  # 返回一个 None 代表没有节点
            node = node.children[ch]
        return node

    # 如果字符串 word 在前缀树中，返回 true 即在检索之前已经插入
    # 否则 返回 false
    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not None and node.isEnd  # 有节点返回 且节点是末端点

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None  # 只要返回就是前缀
