class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        
        for i in range(32):
            bit = n & 1
            out = out | bit
            out = out << 1
            n = n >> 1
        
        return out >> 1