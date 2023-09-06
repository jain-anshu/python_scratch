class Solution:
    def removeDuplicates(self, nums):
      i = 0
      count = 1
      for num in nums:
        if num > nums[i]:
          nums[i + 1] = num
          i += 1
          count += 1
      return count    

vp = Solution()
print(vp.removeDuplicates([1,1,2])  )  