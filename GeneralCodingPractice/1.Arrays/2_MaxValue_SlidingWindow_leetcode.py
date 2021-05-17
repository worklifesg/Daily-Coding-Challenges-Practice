class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      #using max function 
      a = max(nums[:k])
      max_result = [a]
      left = 0

      for i in range(k,len(nums)):
        left+=1
        if nums[left-1] == a:
          if nums[left] >= a-1:
            a = nums[left]
          else:
            a = max(nums[left:i+1])
        new_a = nums[i]
        if new_a > a:
          a = new_a
        max_result.append(a)

      return max_result
'''
Your input
[1,3,-1,-3,5,3,6,7]
3
Output
[3,3,5,5,6,7]
Expected
[3,3,5,5,6,7]

Runtime: 1520 ms, faster than 99.51% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 30.1 MB, less than 51.59% of Python3 online submissions for Sliding Window Maximum.

'''
