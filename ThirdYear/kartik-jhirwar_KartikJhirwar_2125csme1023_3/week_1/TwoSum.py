class Solution:
    def twoSum(self, nums, target):
        mp = {}  
        for i, num in enumerate(nums):
            x = target - num
            if x in mp:
                return [mp[x], i]
            mp[num] = i
        return [-1]
