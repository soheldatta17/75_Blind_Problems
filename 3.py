class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=list(set(nums))
        if len(n)==len(nums):
            return False
        else:
            return True
        