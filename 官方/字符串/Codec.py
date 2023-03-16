# -*- coding: utf-8 -*-

"""
@File    : Codec.py
@Author  : wenhao
@Time    : 2023/3/12 22:58
@LC      : 535
"""
from collections import defaultdict


class Codec:
    def __init__(self):
        self.ids = 0
        self.hash_table = defaultdict(str)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        id = str(self.ids)
        self.ids += 1
        self.hash_table[id] = longUrl
        return id


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash_table[shortUrl]
