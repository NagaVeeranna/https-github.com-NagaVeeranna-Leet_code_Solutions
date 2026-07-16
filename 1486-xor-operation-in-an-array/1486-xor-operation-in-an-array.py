class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            current = start+2*i
            result ^= current
        return result
        