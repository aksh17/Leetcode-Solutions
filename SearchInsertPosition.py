class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                nums.sort()
                ind = nums.index(target)
                return ind
                break
            i += 1
