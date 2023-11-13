class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        a=max(nums)
        if a<=0:
            return a
        s=0
        m=0
        for i in nums:
            s+=i
            if s<0:
                s=0
            m=max(s,m)
        return m