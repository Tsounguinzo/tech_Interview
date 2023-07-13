class Solution(object):
    def removeElement(self, nums, val):
        notVal = 0
        for i in range(len(nums)):
          if nums[i] != val:
            nums[notVal] = nums[i]
            notVal += 1
        return notVal