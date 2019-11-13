class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort()
        nums.reverse()
        print nums
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]
