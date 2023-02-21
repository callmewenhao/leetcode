class Allocator:

    def __init__(self, n: int):
        self.buff = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i, id in enumerate(self.buff):
            if id:
                cnt = 0
            else:
                cnt += 1
                if cnt == size:
                    self.buff[i + 1 - size:i + 1] = [mID] * size
                    return i + 1 - size
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i, id in enumerate(self.buff):
            if id == mID:
                self.buff[i] = 0
                cnt += 1
        return cnt

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
