class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while i < len(nums):
                if i < len(nums)-1 and i+1 <= len(nums)-1:
                    if nums[i] == nums[i+1]:
                        nums.pop(i)
                    else:
                        i += 1
                else:
                    break
        return len(nums)