from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        i = cap = 0
        while True:
            i += 1
            if i < 10:
                tail_len = 5
            elif i < 100:
                if i == 10: cap -= 9
                tail_len = 7
            elif i < 1000:
                if i == 100: cap -= 99
                tail_len = 9
            else:
                if i == 1000: cap -= 999
                tail_len = 11
            if limit - tail_len <= 0: return []
            cap += limit - tail_len
            if cap < n: continue
        # build ans, simulation
        ans = []
        k = 0
        for j in range(1, i + 1):
            tail = f"<{j}/{i}>"
            if j < i:
                m = limit - len(tail)
                ans.append(message[k:k+m] + tail)
                k += m
            if j == i:
                ans.append(message[k:])
        return ans
