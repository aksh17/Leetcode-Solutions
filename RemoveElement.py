class Solution(object):
    def removeElement(self, nums, val):
       i=0
       while i<len(nums):
            if i+1<=len(nums):
                if nums[i]==val:
                    nums.pop(i)
                else:
                    i+=1
            else:
                break
       return len(nums)