class Solution(object):
    def removeDuplicates(self, nums):
      uniqueNumberPosition = 0
      for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
          uniqueNumberPosition += 1
          nums[uniqueNumberPosition] = nums[i]
      return uniqueNumberPosition + 1