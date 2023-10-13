class Solution:
    def maxSubArray(self, nums):
        ans = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum = max(num, num + curr_sum)
            ans = max(ans, curr_sum)
        
        return ans
