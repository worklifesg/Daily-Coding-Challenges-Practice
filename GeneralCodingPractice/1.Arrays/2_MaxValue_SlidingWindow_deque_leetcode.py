from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # let us define result of maximum values stored in an array
        max_result=[]
        #There will be two cases when max value is result itself
        if len(nums)==0:
            return result
        if k > len(nums):
            return result
        
        #we will use deque technique (push/pop operations at both ends and finding the max value)
        
        window = deque()
        
        #to start first we find max of first window
        for i in range(0,k):
            while window and nums[i]>=nums[window[-1]]:
                window.pop()
            window.append(i)
        
        #storing the first max value in the result array
        max_result.append(nums[window[0]])
        
        #Next idea is to slide the window and compare the current stored max value and move forward and repeat steps
        for i in range(k,len(nums)):
            while window and nums[i]>=nums[window[-1]]:
                window.pop()
            #if number doesn't fall in window anymore, remove it
            if window and (window[0]<=i-k):
                window.popleft()
            
            window.append(i)
            max_result.append(nums[window[0]])
            
        return max_result
        
        
 '''
 Your input
[1,3,-1,-3,5,3,6,7]
3
Output
[3,3,5,5,6,7]
Expected
[3,3,5,5,6,7]

Runtime: 1632 ms, faster than 97.21% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 29.9 MB, less than 67.17% of Python3 online submissions for Sliding Window Maximum.
 '''
