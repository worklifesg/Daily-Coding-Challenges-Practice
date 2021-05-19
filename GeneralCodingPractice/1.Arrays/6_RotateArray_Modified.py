class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(start, end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
            
        length = len(nums)
        k = k % length
        
        reverse_array(0,length-1)
        reverse_array(0,k-1)
        reverse_array(k,length-1)

'''
In this program, the reverse array function is defined within the main function and array calling is avoided being twice that improved the runtime
Runtime: 208 ms, faster than 61.91% of Python3 online submissions for Rotate Array.
Memory Usage: 25.6 MB, less than 25.02% of Python3 online submissions for Rotate Array.
'''
