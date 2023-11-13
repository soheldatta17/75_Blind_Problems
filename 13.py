class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(0,n+1):
            if i==0:
                a.append(0)
                continue
            i=str(bin(i))
            a.append(i.count('1'))
        return a