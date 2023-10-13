class Solution:
    def firstIndex(self, nums, low, high, k):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == k:
                if mid == 0 or nums[mid] != nums[mid - 1]:
                    return mid
                else:
                    high = mid - 1
            elif k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def lastIndex(self, nums, low, high, k):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == k:
                if mid == high or nums[mid] != nums[mid + 1]:
                    return mid
                else:
                    low = mid + 1
            elif k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchRange(self, nums, target):
        first_occurrence = self.firstIndex(nums, 0, len(nums) - 1, target)
        last_occurrence = self.lastIndex(nums, 0, len(nums) - 1, target)
        return [first_occurrence, last_occurrence]
