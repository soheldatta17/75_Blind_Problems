from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=prod(nums)
        a=[]
        for i in range (0,len(nums)):
            if nums[i]==0:
                a.append(prod(nums[:i:])*prod(nums[i+1::]))
            else:
                a.append(int(p/nums[i]))
        return a