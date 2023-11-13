class Solution:
    def reverseBits(self, n: int) -> int:
        n=format(n, '032b')
        return int(n[::-1],2)
        