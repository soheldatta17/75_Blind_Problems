class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        # Initialize variables to track max and min products
        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            # Swap max_product and min_product if num is negative
            if num < 0:
                max_product, min_product = min_product, max_product

            # Update max and min products for the current index
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the overall result
            result = max(result, max_product)

        return result
